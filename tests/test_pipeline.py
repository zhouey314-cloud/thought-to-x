import unittest

from thought_to_x.pipeline import PipelineRequest, STAGES, ThoughtToXPipeline
from thought_to_x.providers.base import BaseProvider


class EchoProvider(BaseProvider):
    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        return user_prompt


class PipelineTests(unittest.TestCase):
    def test_stage_order_is_stable(self) -> None:
        self.assertEqual(
            STAGES,
            (
                "normalize", "extract-intent", "find-insight", "tension", "structures",
                "preserve-voice", "x-optimize", "de-ai", "review",
            ),
        )

    def test_pipeline_builds_provider_neutral_prompt(self) -> None:
        pipeline = ThoughtToXPipeline(EchoProvider())
        request = PipelineRequest("这是我的一个零碎想法", output="final-only")
        system, user = pipeline.build_prompts(request)
        lowered = system.lower()
        self.assertIn("preserve the idea", lowered)
        self.assertIn("never fabricate", lowered)
        self.assertIn("de-ai", lowered)
        self.assertIn("output: final-only", user)
        self.assertEqual(pipeline.run(request), user)
