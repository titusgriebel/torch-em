import numpy as np
from torch_em.transform.raw import standardize, normalize_percentile

from torch_em.data.datasets import get_tissuenet_loader
from torch_em.util.debug import check_loader

TISSUENET_ROOT = "/home/pape/Work/data/tissuenet"


def raw_trafo(raw):
    raw = normalize_percentile(raw, axis=(1, 2))
    raw = np.mean(raw, axis=0)
    raw = standardize(raw)
    return raw


# NOTE: the tissuenet data cannot be downloaded automatically.
# you need to download it yourself from https://datasets.deepcell.org/data
def check_tissuenet():
    # set this path to where you have downloaded the tissuenet data
    loader = get_tissuenet_loader(
        TISSUENET_ROOT, "train", raw_channel="rgb", label_channel="cell",
        patch_shape=(512, 512), batch_size=1, shuffle=True,
        raw_transform=raw_trafo
    )
    check_loader(loader, 15, instance_labels=True, rgb=False)


if __name__ == "__main__":
    check_tissuenet()
