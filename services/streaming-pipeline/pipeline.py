import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from transforms import ParseEvent
import sqlite3

DB_PATH = "features.db"


class UpdateFeatures(beam.DoFn):
    def setup(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_features (
                user_id INTEGER,
                item_id INTEGER,
                count INTEGER,
                PRIMARY KEY (user_id, item_id)
            )
        """)
        self.conn.commit()

    def process(self, element):
        user_id, item_id = element

        self.cursor.execute("""
            INSERT INTO user_features (user_id, item_id, count)
            VALUES (?, ?, 1)
            ON CONFLICT(user_id, item_id)
            DO UPDATE SET count = count + 1
        """, (user_id, item_id))

        self.conn.commit()


def run():
    options = PipelineOptions(streaming=False)

    with beam.Pipeline(options=options) as p:
        (
            p
            | "ReadEvents" >> beam.io.ReadFromText("events.jsonl")
            | "Parse" >> beam.ParDo(ParseEvent())
            | "UpdateFeatures" >> beam.ParDo(UpdateFeatures())
        )


if __name__ == "__main__":
    run()
