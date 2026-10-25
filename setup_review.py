"""Extract all downloaded review archives into a single working directory."""
from pathlib import Path
import zipfile

here=Path(__file__).resolve().parent
target=here/'review'
target.mkdir(exist_ok=True)
archives=[here/'source_code.zip']+sorted(here.glob('recorded_data_*.zip'))
if len(archives)<2 or not archives[0].exists():
    raise SystemExit('Download source_code.zip and every recorded_data_*.zip beside this script.')
for path in archives:
    with zipfile.ZipFile(path) as z:
        for entry in z.infolist():
            destination=(target/entry.filename).resolve()
            if target.resolve() not in destination.parents:
                raise ValueError('Invalid archive path')
        z.extractall(target)
print('Ready: cd review; python unpack_artifacts.py; python verify_release.py')
