from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class WikipediaEasy2GreenhouseVsEnantiopure(AbsTaskClassification):
    metadata = TaskMetadata(
        name="WikipediaEasy2GreenhouseVsEnantiopure",
        description="TBW",
        reference="https://wikipedia.org",
        dataset={
            "path": "BASF-We-Create-Chemistry/Wikipedia_Easy_2_Class_Greenhouse_vs_Enantiopure",
            "revision": "92cddec63a3c8ef29dc72ebaba7204625d864a2b",
        },
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="accuracy",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators="derived",
        dialect=[],
        sample_creation=None,
        bibtex_citation=None,
        descriptive_stats={}
    )