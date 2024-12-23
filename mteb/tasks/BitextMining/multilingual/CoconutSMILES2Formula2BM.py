from __future__ import annotations

import datasets

from mteb.abstasks.AbsTaskBitextMining import AbsTaskBitextMining
from mteb.abstasks.MultilingualTask import MultilingualTask
from mteb.abstasks.TaskMetadata import TaskMetadata


class CoconutSMILES2Formula2BM(AbsTaskBitextMining, MultilingualTask):
    metadata = TaskMetadata(
        name="CoconutSMILES2Formula2BM",
        dataset={
            "path": "BASF-We-Create-Chemistry/CoconutSmiles2NameBitextMining2",
            "revision": "5db4895bbfbf84db8e3f876285b5178828f6ebee"
        },
        description="TBW",
        reference="https://coconut.naturalproducts.net/",
        type="BitextMining",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs={
            "en-en": ["en-Latn", "eng-Latn"]
        },
        main_score="f1",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        descriptive_stats={"n_samples": {}, "avg_character_length": {}},
    )

    def load_data(self, **kwargs):
        """Load dataset from HuggingFace hub and convert it to the standard format."""
        if self.data_loaded:
            return

        self.dataset = {}

        for lang in self.hf_subsets:
            self.dataset[lang] = datasets.load_dataset(
                **self.metadata_dict["dataset"])

        self.dataset_transform()
        self.data_loaded = True

    def dataset_transform(self):
        def create_columns(row):
            """Put all English titles in column 'sentence1' and SMILES strings in 'sentence2' column"""
            row["sentence1"] = row["formula"]
            row["sentence2"] = row["smiles"]
            return row

        # Convert to standard format
        for lang in self.hf_subsets:
            self.dataset[lang] = self.dataset[lang].map(create_columns)
