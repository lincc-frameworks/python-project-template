from copier import Worker
import copier_configs.base_configs as bc

def test_thing():
    with Worker(src_path="../", dst_path="../output", data=bc.data_dict) as worker:
        worker.run_copy()