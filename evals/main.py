import argparse
import time
from pathlib import Path

from eval_gui_grounding import GUIGroundingEval
from eval_idm import IDMEval
from eval_idmn2n import IDMN2NEval
from eval_success_detection import SuccessDetectionEval

from agent_studio.llm import setup_model


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--provider", type=str, choices=["openai", "gemini", "claude", "huggingface"]
    )
    parser.add_argument("--model", type=str)
    parser.add_argument("--tokenizer", type=str, default=None)
    parser.add_argument(
        "--eval_type",
        type=str,
        choices=["gui_grounding", "success_detection", "idm", "idmn2n"],
    )
    parser.add_argument("--data_path", type=str)
    parser.add_argument("--start_idx", type=int, default=0)
    parser.add_argument("--end_idx", type=int, default=None)
    parser.add_argument("--num_workers", type=int, default=1)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print(f"Running with args: {args}")

    model = setup_model(args.provider)
    save_path = Path("results")
    save_path.mkdir(parents=True, exist_ok=True)
    # with time
    file_stem = f"{save_path}/{args.eval_type}/{args.model.split('/')[-1]}_{time.strftime('%H%M%S')}"  # noqa: E501
    if args.start_idx != 0:
        file_stem += f"_start{args.start_idx}"
    if args.end_idx is not None:
        file_stem += f"_end{args.end_idx}"
    result_filename = Path(f"{file_stem}.jsonl")

    match args.eval_type:
        case "gui_grounding":
            evaluator = GUIGroundingEval(
                model=model,
                data_path=args.data_path,
                result_filename=result_filename,
                start_idx=args.start_idx,
                end_idx=args.end_idx,
                num_workers=args.num_workers,
            )
        case "success_detection":
            evaluator = SuccessDetectionEval(
                model=model,
                data_path=args.data_path,
                result_filename=result_filename,
                start_idx=args.start_idx,
                end_idx=args.end_idx,
                num_workers=args.num_workers,
            )
        case "idm":  # evaluation on ability as inverse dynamics model
            evaluator = IDMEval(
                model=model,
                data_path=args.data_path,
                result_filename=result_filename,
                start_idx=args.start_idx,
                end_idx=args.end_idx,
                num_workers=args.num_workers,
            )
        case "idmn2n":  # evaluation on inverse dynamics model that predict a sequence of actions from trajectories  # noqa: E501
            evaluator = IDMN2NEval(
                model=model,
                data_path=args.data_path,
                result_filename=result_filename,
                start_idx=args.start_idx,
                end_idx=args.end_idx,
                num_workers=args.num_workers,
            )
        case _:
            raise Exception(f"Unrecoginized eval type: {args.eval_type}")

    if args.tokenizer is None:
        args.tokenizer = args.model

    evaluator(args.model, args.tokenizer)


if __name__ == "__main__":
    main()
