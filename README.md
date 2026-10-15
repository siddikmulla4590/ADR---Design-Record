# SLE Work  — SLE-1, SLE-2, SLE-3 and SLE-4

## Overview

This README summarizes the work documented in my first three SLE submissions and the decision recorded for SLE-4. SLE-1 is a separate rule-based AI Assistant project. SLE-2 and SLE-3 document a Bubble Sort profiling system and its architecture. They are described separately here so the README does not present them as one application.

## SLE-1: Simple AI Agent — Real-life AI Assistant

### Objective
A local Python assistant that responds to everyday user questions without requiring an API key.

### Features
- Responds to supported conversational prompts.
- Provides the current date and time.
- Supports reminders and daily planning.
- Includes a personalized esports response about Jonathan Amaral.
- Uses a simple interactive terminal chat.
- Uses keyword matching to select responses.

### Technology and working
The project is implemented in Python and uses keyword matching to choose a response. The submitted project identifies VS Code AI Copilot as a development assistance tool. No external API key is required.

### Repository
[Open the AI Agent repository](https://github.com/siddikmulla4590/Ai-Agent)

### Project image from the SLE-1 submission

![SLE-1 project image](assets/sle1_image_1.png)

## SLE-2: Profiling Report — Optimized vs. Unoptimized Bubble Sort

### Aim
To profile and compare standard Bubble Sort with an early-stop optimized Bubble Sort using pseudo-random lists of 3,000 integers.

### Algorithms
- **Algorithm A — Unoptimized Bubble Sort:** standard nested-loop comparison approach.
- **Algorithm B — Optimized Bubble Sort:** uses a `swapped` flag and stops early if a full pass makes no swaps.

### Profiling method
- **Workload:** pseudo-random integers generated using `random.randint(1, 100000)`.
- **Iterations:** 10 benchmark runs per algorithm.
- **Fairness:** both versions are run on identical copied datasets.
- **Timing:** Python `time.time()` wall-clock measurement.
- **Profiler:** `py-spy`, using the command recorded in the report:  
  `py-spy record -o profile_flamegraph.svg --rate 100 -- python sort.py`

### Compulsory average-time and profiling results table

| Metric | Algorithm A (Unoptimized) | Algorithm B (Optimized) | Reported comparison |
|---|---:|---:|---|
| Total time (10 runs) | 4.18 seconds | 3.93 seconds | Algorithm B (~6% faster) |
| **Average time per run** | **0.418 seconds** | **0.393 seconds** | **Algorithm B** |
| Total comparisons | 44,985,000 | 44,985,000 | Equivalent |
| Best-case time complexity | O(N²) | O(N) | Algorithm B |
| Worst-case time complexity | O(N²) | O(N²) | Equivalent |

### Observation and analysis
The report records 4.18 seconds for the unoptimized version and 3.93 seconds for the optimized version over 10 runs. The difference is 0.25 seconds in total, approximately 6% of the unoptimized total. On pseudo-random data, the early-stop condition rarely allows the optimized version to finish substantially earlier. These are the measurements recorded for this workload; they should not be taken as a guarantee that the optimized version will always be faster.

## SLE-3: Architectural Design — Full C4 Model

### System title
**Empirical Bubble Sort Profiling System (Optimized vs. Unoptimized)**

The system creates 10 pseudo-random arrays containing 3,000 integers each, runs both Bubble Sort variants on identical copied datasets, measures execution time, and uses `py-spy` to generate a flame graph.

### C4 model levels

1. **Context diagram (Level 1):** shows the Student/Operator starting the workload and the system interacting with the Python runtime and `py-spy`.
2. **Container diagram (Level 2):** separates the Input & Workload Module, Sorting Engine, Benchmark Runner, Profiler, and Results & Visualization.
3. **Component diagram (Level 3):** shows the two sorting functions inside the Sorting Engine. The optimized function adds a `swapped` flag and early termination.
4. **Code-level overview (Level 4):** identifies `bubble_sort_unoptimized(arr)`, `bubble_sort_optimized(arr)`, `run_profiling_workload()`, Python's `random` and `time` modules, and external `py-spy` profiling.

### Design decisions
- Keep the two sorting implementations separate so their performance can be compared.
- Use copied identical datasets to make the benchmark fair.
- Separate workload generation, sorting, timing, and profiling responsibilities.
- Use `py-spy` as an external sampling profiler rather than modifying the sorting code for profiling.

### C4 diagrams from the SLE-3 submission

#### Context diagram — Level 1

![Context diagram — Level 1](assets/sle3_image_1.png)

#### Container diagram — Level 2

![Container diagram — Level 2](assets/sle3_image_2.png)

#### Component diagram — Level 3

![Component diagram — Level 3](assets/sle3_image_3.png)

#### Code-level overview — Level 4

![Code-level overview — Level 4](assets/sle3_image_4.png)

## SLE-4: Decision Record Summary

### Decision
Retain both the unoptimized and early-stop optimized Bubble Sort implementations for comparative performance analysis.

### Rationale
- The unoptimized version provides a baseline for comparison.
- The optimized version demonstrates the effect of the `swapped` flag and early termination.
- SLE-2 records a total of 4.18 seconds for the unoptimized version and 3.93 seconds for the optimized version across 10 runs.
- SLE-3 supports the comparison by separating workload generation, sorting, benchmarking, and profiling.
- The recorded random-data results show a modest difference; they do not establish that the optimized version is always faster.

### Trade-offs and limitations
- Maintaining both implementations requires keeping two functions.
- Pseudo-random inputs may not show the full best-case benefit of early termination.
- Timing results can vary with runtime conditions.
- Both implementations have O(N²) worst-case time complexity.

## AI Contribution Summary

- **SLE-1:** The submitted report names VS Code AI Copilot as a development assistance tool.
- **SLE-2 and SLE-3:** The reports name Gemini and ChatGPT for initial code guidance, profiling-command guidance, C4 architecture/diagram planning, and report formatting.
- The reports state that I configured the environment, ran the profiling workload and `py-spy` commands, generated the flame graph, collected and checked timing results, and reviewed the analysis.

For more detail, see [CONTRIBUTING.md](CONTRIBUTING.md).

## References
1. SLE-1 submission: Simple AI Agent — Real-life AI Assistant.
2. SLE-2 submission: Profiling Report — Optimized vs. Unoptimized Bubble Sort.
3. SLE-3 submission: Architectural Design — Full C4 Model.
4. SLE-4: Architecture Decision Record and the decision summary above.
