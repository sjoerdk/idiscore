from click.testing import CliRunner

import idiscore.cli as cli
from idiscore.annotation import ExampleDataset


def test_cli_to_json(a_path_to_dataset):
    runner = CliRunner()
    assert len(list(a_path_to_dataset.parent.glob("*"))) == 1  # one file in dir

    result = runner.invoke(
        cli.to_dicom_example, [str(a_path_to_dataset)], catch_exceptions=False
    )
    assert result.exit_code == 0  # call should succeed
    dicom_example_path = (
        str(a_path_to_dataset.parent / a_path_to_dataset.stem) + "_template.json"
    )
    with open(dicom_example_path) as f:
        annotated = ExampleDataset.load(f)  # json dataset should be written
    assert annotated.description == "Converted"
