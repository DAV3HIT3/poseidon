import re
import calendar

from atlantis.models import *
from hexmap.models import *

class ParseAtlantisReport:


    def __init__(self, json_report):
        # Save JSON format turn report
        self.json_data = json_report

        # Create regular expression for matching turn error line
        self.turn_error_re = "([\w\s']+)"
        self.turn_error_cre = re.compile(self.turn_error_re)

        # Create regular expression for matching turn event line
        self.turn_event_re = "(?P<unit_name>[\w\s]+)\s*\((?P<unit_id>[\d]+)\)\:?\s*(?P<event_msg>[\w\s()'$,:%;\[\]]+\.?)"
        #self.turn_event_re = "([\w\s$',\.\[\]]+)"
        self.turn_event_cre = re.compile(self.turn_event_re)

        # Create dictionay lookup for (month name, month number)
        self.month_lookup = {v: k for k,v in enumerate(calendar.month_name)}

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

    def parseFactionInfo(self, report_section):
        self.faction_name = ""
        self.faction_id = ""
        self.faction_war_pt = 0
        self.faction_trade_pt = 0
        self.faction_magic_pt = 0
        if "factionName" in report_section:
            self.faction_name = report_section["factionName"]
        if "factionNumber" in report_section:
            self.faction_id = report_section["factionNumber"]
        if "points" in report_section:
            self.faction_war_pt = report_section["points"]["war"]
            self.faction_trade_pt = report_section["points"]["trade"]
            self.faction_magic_pt = report_section["points"]["magic"]

        # Lookup faction id DB or create if not existing
        self.faction, created = Faction.objects.get_or_create(name=self.faction_name, faction_id=self.faction_id)
        self.default_attitude, created = Attitude.objects.get_or_create(name="NEUTRAL")
        self.user_faction, created = UserFaction.objects.get_or_create(user=self.user,
                                                              faction=self.faction,
                                                              war_points=self.faction_war_pt,
                                                              trade_points=self.faction_war_pt,
                                                              magic_points=self.faction_war_pt,
                                                              default_attitude=self.default_attitude)


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
                
    def parseFactionStatus(self, report_section):
        # TODO: check unit counts vs report counts...
        pass

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
            

    def parseEvents(self, report_section):
        event_list = ""
        if "events" in report_section:
            event_list = report_section["events"]
            for event_line in event_list:
                match = self.turn_event_cre.search(event_line)
                #if len(match) == 1:
                #    event_msg = match[0]
                #    turn_event = TurnEvent.objects.create(user_turn=self.user_turn,
                #                                          text=event_line,
                #                                          event_msg=event_msg)

                #elif len(match) >= 3:
                #    unit_name = match[0]
                #    unit_id = match[1]
                #    event_msg = match[2]
                if match:
                    unit_name = match.group('unit_name')
                    unit_id = match.group('unit_id')
                    event_msg = match.group('event_msg')
            
                    unit,created = Unit.objects.get_or_create(unit_id=unit_id)
                    turn_event = TurnEvent.objects.create(user_turn=self.user_turn,
                                                          text=event_line,
                                                          unit=unit,
                                                          event_msg=event_msg)
 

    def parseSkills(self, report_section):
        pass

    def parseItemReports(self, report_section):
        pass

    def parseObjectReports(self, report_section):
        pass

    def parseAttitudes(self, report_section):
        pass

    def parseUnclaimedSilver(self, report_section):
        pass

    def parseRegions(self, report_section):
        pass

    def parseOrdersTemplate(self, report_section):
        pass


