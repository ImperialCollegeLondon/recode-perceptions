import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd
import torch


def argument_parser(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--epochs", default=20, type=int, help="number of training epochs"
    )
    parser.add_argument(
        "--batch_size", default=128, type=int, help="batch size for SGD"
    )
    parser.add_argument("--model", default="resnet101", type=str, help="model_loaded")
    parser.add_argument(
        "--pre", default="resnet", type=str, help="pre processing for image input"
    )
    parser.add_argument(
        "--root_dir",
        default=Path(__file__).parent.parent,
        help="path to recode-perceptions",
    )
    parser.add_argument("--lr", default=1e-3, type=float, help="learning rate")
    parser.add_argument(
        "--study_id",
        default="50a68a51fdc9f05596000002",
        type=str,
        help="perceptions_1_to_6",
    )
    parser.add_argument(
        "--run_name",
        default="default",
        type=str,
        help="unique name to identify hyperparameter choices",
    )
    parser.add_argument("--data_dir", default="input/images/", type=str, help="dataset")
    parser.add_argument("--verbose", default=False, type=bool, help="intermed. outputs")
    return parser.parse_args(args)


def detect_device():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Running on %s device" % device)
    return device


def output_plots(results, root_dir, run_name):
    df = pd.DataFrame(results)
    save_path = (
        root_dir
        / "outputs"
        / "results"
        / (run_name + f"{datetime.now().strftime('%Y%m%d_%H-%M-%S')}.log" + ".csv")
    )
    df.to_csv(save_path)


def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].reshape(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res
