import apache_beam as beam
import json


class ParseEvent(beam.DoFn):
    def process(self, element):
        try:
            event = json.loads(element)
            yield (event["user_id"], event["item_id"])
        except Exception:
            return
