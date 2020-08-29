import re, calendar, sys

from atlantis.models import *
from hexmap.models import *

class ParseAtlantisReport:

    # ---------------------------------------------------------------------------------------------------------------------
    # Initialize report parser
    # ---------------------------------------------------------------------------------------------------------------------
    def __init__(self, json_report):
        # Save JSON format turn report
        self.json_data = json_report

        # Create regular expression for matching turn error line
        self.turn_error_re = "([\w\s']+)"
        self.turn_error_cre = re.compile(self.turn_error_re)

        # Create regular expression for matching turn event line
        self.turn_event_re = "(?P<unit_name>[\w\s]+)\s*\((?P<unit_id>[\d]+)\)\:?\s*(?P<event_msg>[\w\s()'$,:%;\[\]]+\.?)"
        self.turn_event_cre = re.compile(self.turn_event_re)

        # Attitudes
        self.turn_attitude_re = "(?P<attitude_name>[\w]+)\s+:\s+(?P<faction_list>[\w\s\(\),]+)"
        self.turn_attitude_cre = re.compile(self.turn_attitude_re)

        # Faction name & id
        self.faction_re = "(?P<faction_name>[\w\s]+)\s*(\(?(?P<faction_id>[\d]+)?\))?"
        self.faction_cre = re.compile(self.faction_re)

        # Create dictionay lookup for (month name, month number)
        self.month_lookup = {v: k for k,v in enumerate(calendar.month_name)}

        # This parser was written to the following Atlantis version
        self.parser_atlantis_version = "5.2.4 (beta)"
        # This parser was written to the following engine version
        self.parser_engine_version = "2.0.0 (beta)"

        # ========================
        # Variables used by parser
        self.faction_obj = {}
        self.user_faction_obj = {}

    # ---------------------------------------------------------------------------------------------------------------------
    # Main atlantis report (JSON format) parser function
    #
    # Each section is parsed by its corresponding method.
    # Django model database calls are used to update or create the appropriate
    # mdoel instances.
    #
    # Current parser version: Atlantis 5.2.4 (beta), NewOrigins v2.0.0 (beta) 
    # Parser created: August, 2020
    # ---------------------------------------------------------------------------------------------------------------------
    def parseJson(self, user):
        self.user = user
        for report_section in self.json_data:
            if "type" in report_section:
                if report_section["type"] == "FACTION_INFO":
                    self.parseFactionInfo(report_section)
                elif report_section["type"] == "DATE":
                    self.parseDate(report_section)
                elif report_section["type"] == "VERSIONS":
                    self.parseVersion(report_section)
                elif report_section["type"] == "FACTION_STATUS":
                    self.parseFactionStatus(report_section)
                elif report_section["type"] == "ERRORS":
                    self.parseErrors(report_section)
                elif report_section["type"] == "EVENTS":
                    self.parseEvents(report_section)
                elif report_section["type"] == "BATTLES":
                    self.parseBattles(report_section)
                elif report_section["type"] == "SKILLS":
                    self.parseSkills(report_section)
                elif report_section["type"] == "ITEM_REPORTS":
                    self.parseItemReports(report_section)
                elif report_section["type"] == "OBJECT_REPORTS":
                    self.parseObjectReports(report_section)
                elif report_section["type"] == "ATTITUDES":
                    self.parseAttitudes(report_section)
                elif report_section["type"] == "UNCLAIMED_SILVER":
                    self.parseUnclaimedSilver(report_section)
                elif report_section["type"] == "REGIONS":
                    self.parseRegions(report_section)
                elif report_section["type"] == "ORDERS_TEMPLATE":
                    self.parseOrdersTemplate(report_section)
                else:
                    print("WARNING! Unknown report section" + report_section["type"])

    # ---------------------------------------------------------------------------------------------------------------------
    # Faction info contains basic faction name, id, and war, trade, & magic points
    # Creates faction, and logged-in user's faction if not existing
    #
    # Note: attitudes are parsed in parseAttitude section
    # ---------------------------------------------------------------------------------------------------------------------
    def parseFactionInfo(self, report_section):

        if "factionName" in report_section:
            self.faction_obj["name"] = report_section["factionName"]
        if "factionNumber" in report_section:
            self.faction_obj["faction_id"] = report_section["factionNumber"]
        if "points" in report_section:
            if "war" in report_section["points"]:
                self.user_faction_obj["war_points"] = report_section["points"]["war"]
            if "trade" in report_section["points"]:
                self.user_faction_obj["trade_points"] = report_section["points"]["trade"]
            if "magic" in report_section["points"]:
                self.user_faction_obj["magic_points"] = report_section["points"]["magic"]


        # Lookup faction id DB or create if not existing
        self.faction, created = Faction.objects.get_or_create(**self.faction_obj)
        self.user_faction_obj["user"] = self.user
        self.user_faction_obj["faction"] = self.faction
        self.user_faction, created = UserFaction.objects.get_or_create(**self.user_faction_obj)

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse the turn date (year & month)
    #
    # TODO: figure out the turn number, currently blank
    # ---------------------------------------------------------------------------------------------------------------------
    def parseDate(self, report_section):
        self.turn_number = ""
        self.month = ""
        self.year = ""
        self.unclaimed_silver = 0
        if "month" in report_section:
            self.month = self.month_lookup[report_section["month"]]
        if "year" in report_section:
            self.year = report_section["year"]

        self.turn, created = Turn.objects.get_or_create(month=self.month, year=self.year)

        self.user_turn, created = UserTurn.objects.get_or_create(user_faction=self.user_faction,
                                                                 turn=self.turn,
                                                                 unclaimed_silver=self.unclaimed_silver)

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse atlantis version info
    # TODO: Raise exception if report version doesn't match version parser can handle
    # ---------------------------------------------------------------------------------------------------------------------
    def parseVersion(self, report_section):
        self.atlantis_version = ""
        self.engine_name = ""
        self.engine_version = ""
        if "atlantisVersion" in report_section:
            self.atlantis_version = report_section["atlantisVersion"]
        if "engineName" in report_section:
            self.engine_name = report_section["engineName"]
        if "engineVersion" in report_section:
            self.engine_version = report_section["engineVersion"]

        # TODO: raise exception if version numbers don't match parser...
        
                
    # ---------------------------------------------------------------------------------------------------------------------
    # Faction status
    # TODO: Check report faction status counts, i.e. Number of trade regions,
    # quartermasters, mages, etc. These should be compared with internal counts
    # for those units, regions, etc...
    # ---------------------------------------------------------------------------------------------------------------------
    def parseFactionStatus(self, report_section):
        # TODO: check unit counts vs report counts...
        pass

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse turn errors
    # TODO: use named groups in regex
    #
    # Note: unit is created if not exists
    # ---------------------------------------------------------------------------------------------------------------------
    def parseErrors(self, report_section):
        error_list = ""
        if "errors" in report_section:
            error_list = report_section["errors"]
            for error_line in error_list:
                match = self.turn_error_cre.findall(error_line)
                if len(match) == 4:
                    error_unit_name = match[0]
                    error_unit_id = match[1]
                    error_type = match[2]
                    error_msg = match[3]
            
                    unit,created = Unit.objects.get_or_create(unit_id=error_unit_id)
                    turn_error = TurnError.objects.create(user_turn=self.user_turn,
                                                          text=error_line,
                                                          unit=unit,
                                                          error_type=error_type,
                                                          error_msg=error_msg)
            

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse turn events
    #
    # Note unit is created if not exists
    # ---------------------------------------------------------------------------------------------------------------------
    def parseEvents(self, report_section):
        event_list = ""
        if "events" in report_section:
            event_list = report_section["events"]
            for event_line in event_list:
                match = self.turn_event_cre.search(event_line)
                if match:
                    unit_name = match.group('unit_name')
                    unit_id = match.group('unit_id')
                    event_msg = match.group('event_msg')
            
                    unit,created = Unit.objects.get_or_create(unit_id=unit_id)
                    turn_event = TurnEvent.objects.create(user_turn=self.user_turn,
                                                          text=event_line,
                                                          unit=unit,
                                                          event_msg=event_msg)
 

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse battle report - Currently ignored
    # ---------------------------------------------------------------------------------------------------------------------
    def parseBattles(self, report_section):
        pass

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse skill report - Currently ignored
    # ---------------------------------------------------------------------------------------------------------------------
    def parseSkills(self, report_section):
        pass

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse item report - Currently ignored
    # ---------------------------------------------------------------------------------------------------------------------
    def parseItemReports(self, report_section):
        pass

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse object report - Currently ignored
    # ---------------------------------------------------------------------------------------------------------------------
    def parseObjectReports(self, report_section):
        pass

    # ---------------------------------------------------------------------------------------------------------------------
    # Parse current faction attitudes toward other factions & default attitude
    #
    # TODO: needs more work...
    # ---------------------------------------------------------------------------------------------------------------------
    def parseAttitudes(self, report_section):
        attitude_list = ""
        default_attitude = ""
        if "default" in report_section:
            default_attitude = report_section["default"]
        elif "attitudes" in report_section:
            attitude_list = report_section["attitudes"]
            for attitude_line in attitudes_list:
                match = self.turn_attitude_cre.search(attitude_line)
                if match:
                    attitude_name = match.group('attitude_name')
                    faction_list = match.group('faction_list')

                    faction_match = self.faction_cre.findall(faction_list)
                    if len(faction_match) == 1:
                        faction = faction_match[0]
                        if faction != "none":
                            print("WARNING! Unexpected faction attitude: [" + attitude_line + "]")

                    elif len(faction_match) > 1:
                        print(faction_match)


                    unit,created = Unit.objects.get_or_create(unit_id=unit_id)
                    turn_event = TurnEvent.objects.create(user_turn=self.user_turn,
                                                          text=event_line,
                                                          unit=unit,
                                                          event_msg=event_msg)

        pass

    # ---------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------
    def parseUnclaimedSilver(self, report_section):
        if "amount" in report_section:
            unclaimed_silver  = report_section["amount"]
            self.user_turn.unclaimed_silver = unclaimed_silver
            self.user_turn.save()

    # ---------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------
    def parseRegions(self, report_section):
        if "regions" in report_section:
            region_list = report_section["regions"]
            for region in region_list:
                region_obj = {}
                if "title" in region:
                    region_obj["name"] = region["title"]
                    #print(region_obj["name"], file=sys.stderr)
                if "coordinates" in region:
                    coordinate = region["coordinates"]
                    coord, created = Point.objects.get_or_create(**coordinate)
                    region_obj["coordinate"] = coord
                if "type" in region:
                    region_typename = region["type"][0]
                    region_type, created = RegionType.objects.get_or_create(name=region_typename)
                    region_obj["region_type"] = region_type

                #print(region_obj, file=sys.stderr)
                region_rec, created = Region.objects.get_or_create(**region_obj)

                

    # ---------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------
    def parseOrdersTemplate(self, report_section):
        pass


