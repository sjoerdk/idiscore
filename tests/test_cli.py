from click.testing import CliRunner
from dicomgenerator.export import export

import idiscore.cli as cli
from idiscore.annotation import ExampleDataset


def test_cli_to_example(a_path_to_dataset):
    runner = CliRunner()
    assert len(list(a_path_to_dataset.parent.glob("*"))) == 1  # one file in dir

    result = runner.invoke(
        cli.to_example, [str(a_path_to_dataset)], catch_exceptions=False
    )
    assert result.exit_code == 0  # call should succeed
    dicom_example_path = (
        str(a_path_to_dataset.parent / a_path_to_dataset.stem) + "_template.json"
    )
    with open(dicom_example_path) as f:
        annotated = ExampleDataset.load(f)  # json dataset should be written
    assert annotated.description == "No description"


def test_cli_to_dicom(tmp_path_factory, a_dataset):
    root = tmp_path_factory.mktemp("to_dicom")
    json_file = root / "a_dicom_example.json"
    with open(json_file, "w") as f:
        ExampleDataset(dataset=a_dataset).save(f)

    runner = CliRunner()
    result = runner.invoke(cli.to_dicom, [str(json_file)], catch_exceptions=False)
    assert result.exit_code == 0  # call should succeed


def test_cli_to_example_temp(tmp_path, a_path_to_dataset):
    runner = CliRunner()
    result = runner.invoke(
        cli.to_example, [str(a_path_to_dataset)], catch_exceptions=False
    )
    assert result.exit_code == 0  # call should succeed
    dicom_example_path = (
        str(a_path_to_dataset.parent / a_path_to_dataset.stem) + "_template.json"
    )
    with open(dicom_example_path) as f:
        annotated = ExampleDataset.load(f)  # json dataset should be written
    assert annotated.description == "No description"

    export(annotated.dataset, path=tmp_path / "test_cli_to_example_temp.dcm")
