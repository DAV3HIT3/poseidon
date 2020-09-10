from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Build javascript grammar for the report parser'

    base_dir = Path("report_parser/static/report_parser/js/")

    def build_grammar_basic(self):
        grammar_file = self.base_dir / "grammar-base/index.ne"
        output_file = self.base_dir / "grammar-base-compiled.js"
        command = "nearleyc " + str(grammar_file) + " -o " + str(output_file)
        os.system(command)

    #def build_grammar_unit(self):
    #    grammar_file = self.base_dir / "grammar-unit/index.ne"
    #    output_file = self.base_dir / "grammar-unit-compiled.js"
    #    command = "nearleyc " + str(grammar_file) + " -o " + str(output_file)
    #    os.system(command)

    #def build_grammar_unit_event(self):
    #    grammar_file = self.base_dir / "grammar-unit-event/index.ne"
    #    output_file = self.base_dir / "grammar-unit-event-compiled.js"
    #    command = "nearleyc " + str(grammar_file) + " -o " + str(output_file)
    #    os.system(command)

    def build_grammar_all(self):
        self.build_grammar_basic()
        #self.build_grammar_unit()
        #self.build_grammar_unit_event()

    def handle(self, *args, **options):
        self.build_grammar_all()

