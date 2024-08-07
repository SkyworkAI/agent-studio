<h1 align="center">
AgentStudio
</h1>

<p align="center">
<a href='https://arxiv.org/abs/2403.17918'><img src='https://img.shields.io/badge/arXiv-2403.17918-b31b1b.svg'></a>
<a href='https://skyworkai.github.io/agent-studio/'><img src='https://img.shields.io/badge/Project-Page-Green'></a>
<a href="https://www.python.org/downloads/release/python-3117/"><img alt="Python 3.11" src="https://img.shields.io/badge/python-3.11-blue.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<!-- <a href="https://mypy-lang.org/"><img src="https://www.mypy-lang.org/static/mypy_badge.svg" alt="Checked with mypy"></a> -->
<a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" alt="License: AGPL v3"></a>
<a href="https://pre-commit.com/"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit"></a>
</p>

AgentStudio is an integrated solution featuring in-depth benchmark suites, realistic environments, and comprehensive toolkits. Here, we open-source everything to promote research towards generalist computer agents of the future. The paper, leaderboard, benchmark suites, and documentation for environments and toolkits can be found in our <a href="https://skyworkai.github.io/agent-studio/"><b>project page</b></a>.

![](docs/assets/overview.png)

Comparisons with existing work:

![](docs/assets/comparison.png)

## Install

Please see [docs/install.md](docs/install.md) for more details. We are going to create a packed release for out-of-box usage.

## Three Offline Benchmark Suites

We curated three static datasets for benchmarking GUI grounding, success detection, and learning from videos, respectively. Please see the detailed [evals/README.md](evals/README.md) for scripts that reproduce the benchmark results in our paper.

## Customize Online Benchmarks in Real Environments

![](docs/assets/agent_space.jpg)

AgentStudio also provides a cross-platform real-world environments with most generic (human-like) observation and action spaces. We also offer a set of example tasks as a demonstration to benchmark computer agents in the wild. We also offer several auto-evaluators for easily benchmark without human evaluation. The implementation is straightforward and flexible, supporting adding custom tasks as well as human evaluation. Please find more in [docs/online_benchmark.md](docs/online_benchmark.md).

## Record GUI Data and Trajectories

The real-world environments also facilitate scalable data collection across different operating systems. AgentStudio offers two data collection pipelines for single-step GUI grounding data and task-completing trajectories, for both local recording (assuming there are two screens) and remote recording (based on VNC). Please refer to the [docs/annotate_ground_ui.md](docs/annotate_ground_ui.md) and [docs/annotate_trajectory.md](docs/annotate_trajectory.md) for detailed instructions.

Here is an example of recording single-step GUI grounding data in MacOS:

![](docs/assets/annotate_gui_2.jpg)

## Contributing

We are continuing to expand the collection of environments, tasks, and data over time. Contributions and feedback from everyone on how to make this into a better tool are more than welcome. Please check out [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.

## Acknowledgement

We would like to thank the following projects for their inspiration and contributions to the open-source community: [Open Interpreter](https://github.com/KillianLucas/open-interpreter), [WebArena](https://github.com/web-arena-x/webarena), [Cradle](https://baai-agents.github.io/Cradle/), [Synapse](https://ltzheng.github.io/Synapse/), [SeeClick](https://github.com/njucckevin/SeeClick), [ScreenAgent](https://github.com/niuzaisheng/ScreenAgent), etc.

## Citation

If you find AgentStudio useful, please cite our [paper](https://arxiv.org/abs/2403.17918):

```bibtex
@article{zheng2024agentstudio,
  title={AgentStudio: A Toolkit for Building General Virtual Agents},
  author={Longtao Zheng and Zhiyuan Huang and Zhenghai Xue and Xinrun Wang and Bo An and Shuicheng Yan},
  journal={arXiv preprint arXiv:2403.17918},
  year={2024}
}
```
