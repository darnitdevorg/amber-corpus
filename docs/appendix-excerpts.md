

## usenixsec2022-final7 — Automated Side Channel Analysis of Media Software with Manifold Learni
- artifact: https://zenodo.org/record/5816702#.YdQMHxNByjA
- ref: zenodo_record 5816702
- paper: https://www.usenix.org/conference/usenixsecurity22/presentation/yuan-yuanyuan

```
media software and localize side channel vulnerabilities of
the target software. We also provide a mitigation scheme towards our attack and investigate the noise resilience of our
attacking technique.

A.2


• Hardware. We perform Prime+Probe attacks on Intel Xeon
and AMD Ryzen CPUs. Nevertheless, our approach is not
hardware-specific. Users can use our tools on other CPUs. To
approximate manifold from known data (i.e., the training split),
users are recommended to run scripts on GPUs. Note that our
tool requires a relatively large RAM.

side channel vulnerabilities of media software.
We release 1) scripts for logging side channels and our logged
side channel records; 2) scripts for training models and our
trained models; 3) scripts for reconstructing media data from
unknown side channels (i.e., the test split) and our reconstructed media data; 4) scripts for localizing side channel vulnerabilities and our localized vulnerabilities. Some vulnerabilities have been explored by previous works, and the new-found
vulnerabilities have been confirmed by developers of FFmpeg

• How much disk space required (approximately)? We provide 1K samples of processed data and side channel records for
each dataset and software. We also provide our trained models

• Experiments. We provide 1K samples of processed data and
side channel records for each dataset and software. These samples are sufficient to verify our statements and results, for instance, reconstructing high-quality media data from side channel records and mitigating side channel attack using perception
blinding (e.g., perceptual properties of reconstructed images

• How much time is needed to prepare workflow/complete
experiments (approximately)?
1) Set up the environment: less than 1 hour. We also provide a
docker container with everything set up.
2) Download public datasets and process: it requires less than
1 hour to process the data. We provide our processed data

of all media and target software. We provide our logged side
channels.
4) Train models: training one model requires less than 24 hours
on one Nvidia GeForce RTX 2080 GPU. Our script also supports training on CPUs, but it could be time-consuming. We
also release our trained models.
5) Others: a few minutes.

We show that side channel analysis (SCA) towards media software can be largely boosted by manifold learning, which recasts
SCA as mapping between side channels and media data via a lowdimensional joint manifold. Enabled by the neural attention mechanism, we can localize side channel vulnerabilities of media software
by investigating which records on a logged side channel trace contribute most to the reconstruction of media data. Our findings have
been confirmed by the software developers. We further propose the
perception blinding that is highly effective for mitigating manifold
learning-based side channel attacks. We also show that our approach

side channel records of the target software when it is processing
private data. Based on the collected side channels and corresponding
media data, users can train a model to appropriate the manifold.
The trained model can reconstruct high-quality media data from unknown side channels (i.e., the test split of each dataset). We provide
our trained models and 1K data samples (from test split). Using
our trained models, users can observe that the reconstructed media

can customize 1) the media datasets, 2) hardware platforms, 3) target
software, 4) model architectures, 5) training parameters when appropriating manifold, 6) blinding masks, 7) noise insertion schemes.
We provide APIs for customized settings; see details in README.

```


## usenixsec2022-final15 — Synthetic Data – Anonymisation Groundhog Day
- artifact: https://github.com/spring-epfl/synthetic_data_release/tree/v1.1
- ref: tag v1.1
- paper: https://www.usenix.org/conference/usenixsecurity22/presentation/stadler

```
11.4.2, along with all dependencies required by Synthetic Data.
• Hardware: When running evaluations for either the PATE-GAN
or CTGAN model it is useful to have a GPU at hand. This significantly speeds up the execution. However, they are not needed
for running the example experiments.
• Execution: The README includes instructions about how
to run three example experiments. The evaluation under the

• How much time is needed to complete experiments (approximately)?: This depends on the compute power available.
On a machine with an Intel(R) Core(TM) i7-7600U CPU @
2.80GHz with 2 cores (with hyperthreading) it should take 3h
to run all example experiments.
• Publicly available?:
The code is publicly available

Dependencies

• Output: The example experiments produce output files in a
json format and can be parsed with the functions provided
in utils/analyse_rersults. We include a simple jupyter
notebook that allows to visualise and analyse the results.

with all dependencies required by Synthetic Data.
Note: This distribution includes CUDA binaries, before downloading the image, ensure to read its EULA and to agree to its terms.

• Experiments: The repository includes experiment configuration for three key experiments. See further below of the
README of the repository.


• How much disk space required (approximately)?: If using
the dockerised deployment, its image requires 1̃4GB of disk
space. The experiment outputs need
• How much time is needed to prepare workflow (approximately)?: <1h (but strongly depends on the bandwidth of the
connection used to pull the Docker image).


```


## usenixsec2022-final9 — Arbiter: Bridging the Static and Dynamic Divide in Vulnerability Disco
- artifact: https://github.com/jkrshnmenon/arbiter/releases/tag/v1.1
- ref: tag v1.1
- paper: https://www.usenix.org/conference/usenixsecurity22/presentation/vadayath

```
The software requirements for installing are Python (version
at least 3.8) and angr. The artifact has been tested on a machine running Ubuntu 18.04. The artifact also contains the
list of packages that were used for evaluation, a JSON file
containing the MD5 hashes of each of the binaries as well as
the actual binaries from the Juliet data set that were evaluated.
Our paper describes A RBITER as a combination of static

• Hardware: Our experiments were performed on a kubernetes
cluster where each pod was provided 1 logical core and 4 GB
of RAM. However, each pod could request up to 8 GB of RAM.
• Execution: The artifact contains a helper script that can be
executed using the Python interpreter. The arguments to this
script include the VD template to use as well as the target

• How much disk space required (approximately)?: The total disk space used, including downloaded binaries and generated output files, for our experiment is approximately 350
GB.
• How much time is needed to prepare workflow (approximately)?: Installing the framework or using the docker container should take nearly 5 minutes. However, downloading
the binaries could take up to 1 minute per package. Even if this
process is performed in parallel, it could take up to 1 hour to
download all the packages depending upon the network speed.

• How much time is needed to complete experiments (approximately)?: Our evaluation was performed on a kubernetes cluster that allowed running 800 tasks at a time. With
that constraint, our evaluation of 76,516 binaries took nearly 2
days to complete per template.
• Publicly
available
(explicitly

Hardware dependencies

The artifact requires 1 logical core and at least 4 GB of RAM.

A.3.3


Software dependencies

The artifact has been verified to work on Ubuntu 18.04 and requires
Python (at least version 3.8) and the angr python package.

A.3.4

```


## usenixsec2022-final5 — CellIFT: Leveraging Cells for Scalable and Precise Dynamic Information
- artifact: https://github.com/comsec-group/cellift-artifacts/tree/eaa9a26ae85fd6a7ae8cd248416315414ae4c135
- ref: commit eaa9a26ae85fd6a7ae8cd248416315414ae4c135
- paper: https://www.usenix.org/conference/usenixsecurity22/presentation/solt

```
native RISC-V toolchain, and other dependencies. We also
provide the framework for performing all the experiments
described in this paper and analyzing the obtained results. Everything is packaged as a Docker image to allow for optimal
reproducibility. To reproduce the experiments, we expect a
machine with 256 GB memory and 500 GB of free storage.


targets, as well as benchmarks from the RISC-V Architectural
testing framework. All of this code is included in our artifact.
• Compilation: We include the required compilers and interpreters.
• Transformations: We include the required Verilog transformations (CELLIFT and GLIFT), implemented as Yosys passes.
• Binary: We include prebuilt Verilator binaries of the five CPU
designs in all instrumentation modes (i.e., vanilla, CELLIFT,

• Hardware: We do not require any special hardware, but do
need a relatively large amount of DRAM (256 GB) to run all
the experiments.

• How much time is needed to prepare workflow: To prepare
the workflow, conscious effort is only needed to retrieve the

• How much time is needed to complete experiments: Reproducing the experiments takes approximately 3 days.
• Publicly available: Stable URL: https://github.com/c
omsec-group/cellift-artifacts/commit/eaa9a26a
e85fd6a7ae8cd248416315414ae4c135. The README
points to a stable (sha256-verified) Dockerhub Docker image
that contains the rest of the code and data, namely docker.i

Hardware dependencies

The artifact will run all experiments on a machine with 256 GB of
memory.

A.3.3

Software dependencies

• Metrics: The experiments record runtime performance and
IFT precision for microbenchmarks for CELLIFT as well as
GLIFT. Further experiments record execution time and memory footprint of the instrumentation and synthesis process for
all instrumentation modes. We also measure the simulation

• How much disk space required: The docker image with
all the layers is 330 GB, and Xilinx Vivado requires around
150 GB for downloading and installation. In total, we estimate
a total of 500 GB of free storage is required.

A.4

plot_benchmark_performance.py).
3. The Meltdown and Spectre simulations reproduce Figure
11, showing they can both be detected (follows from
plot_tainted_elements.py).
4. We show several bug scenarios detected by CELLIFT
(run_scenarios.sh).

```


## usenixsec2022-final26 — A Hardware-Software Co-design for Efficient Intra-Enclave Isolation
- artifact: 
- ref:  
- paper: https://www.usenix.org/conference/usenixsecurity22/presentation/gu-jinyu

```
Hardware dependencies

The artifact evaluation requires an Intel x86 platform that supports
Intel SGX, PKU and MPX. Our remote machine has an Intel i710700 IceLake CPU.

A.3.3

Software dependencies

Except for the environment mentioned in the checklist, L IGHT E N CLAVE requires the building system and toolchain from Occlum and
Graphene-SGX. To save the time for reviewers, we have prepared
the software dependencies for the artifact evaluation in the offered
machine.

• Hardware: An Intel x86 platform that supports Intel SGX,
PKU and MPX.
• Run-time environment: The experiment is carried out on
Linux. The kernel should set CR4.FSGSBASE = 1 to allow
userspace applications use wrfsbase and wrgsbase to modify
fs.base and gs.base. On newer versions of Linux (>= 5.9),

• How much disk space required (approximately): Around
18G. We suggest different AE reviewers use different working
directories. Since the disk space of our remote machine is
limited, please remove the working directory once the artifact
evaluation completes (in case leading to out-of-disk for others).


We provide a remote machine with software dependencies prepared,
where reviewers can start from the installation stage. Please check
Artifact access in the submission (on hotcrp) for detail.
After login into the machine, the home directory contains the
lightenclave-artifact directory that holds evaluation materials. Before starting the evaluation, please copy lightenclave-artifact to another directory to avoid conflicts between different reviewers.
> sudo cp -r lightenclave - artifact your evaluation - directory

• How much time is needed to prepare workflow (approximately): We provide a remote machine which is setted up for
artifact evaluation so that reviewers do not need to prepare the
workflow.

> bash build_occlum_apps_in_docker . sh
# Now inside the docker

• How much time is needed to complete experiments (approximately): The building procedure is about 1 hour. The
complete evaluation takes about 3 hours.

Then we build applications running inside Graphene using another docker environment. This docker environment is used in the



as it consumes large disk space.
> sudo rm -rf your - evaluation - directory

A.9

Version

```


## usenixsec2023-final21 — Decompiling x86 Deep Neural Network Executables
- artifact: https://github.com/monkbai/DNN-decompiler/tree/b4f64783846b85cac4b0eb6c7a5595535cc858d3
- ref: commit b4f64783846b85cac4b0eb6c7a5595535cc858d3
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/liuzhibo

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


than 120GB of disk space. Besides, the symbolic execution
may consume a lot of memory resources, so please make sure
that the machine on which the experiment is run has sufficient
memory.
A.2.4


Software dependencies

BTD relies on IDA Pro (version 7.5) for disassembly, and
because IDA is commercial software, we do not provide it in
this repo; instead, in order to reduce the workload of AE reviewers, we provide the disassembly results directly as input
for BTD. The scripts used to disassemble DNN executable

Benchmarks
Table 1: Compilers evaluated in our study.

Tool Name

Publication

Hardware dependencies

We ran our evaluation experiments on a server equipped
with Intel Xeon CPU E5-2683, 256GB RAM, and an Nvidia
GeForce RTX 2080 GPU. Logging and filtering all traces
for all DNN executables in the evaluation takes more than a

```


## usenixsec2023-final36 — IvySyn: Automated Vulnerability Discovery in Deep Learning Frameworks
- artifact: https://gitlab.com/brown-ssl/ivysyn/-/tree/4b3d26dda0ddea11282c2658e28090a738dfd6c7
- ref: commit 4b3d26dda0ddea11282c2658e28090a738dfd6c7
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/christou

```
reproduce the results of IvySyn, along with information regarding system and resource requirements.

A.2

Description & Requirements


Hardware dependencies

The provided Docker images are configured to use 4 CPUs
and 16GB of RAM, but can also be set to use fewer (or more)
resources, as needed.
A.2.4

Software dependencies

We provide a Docker image that builds and runs IvySyn, and
hence Docker is required. Some scripts run outside Docker
containers and were tested on Debian v11—but they are relatively simple and should work on any Linux distribution.


Benchmarks

All the data required for running our benchmarks are either
included in the project repository or can be produced by our
scripts during setup. Note that the prototype implementation
of IvySyn fuzzes both CPU- and GPU-specific implementations of DL kernels. However, we are not able to provide

access to machines with GPUs. Therefore, the benchmarks
in the artifact fuzz only kernels with CPU implementations.
This does not have any effect on the claims of the paper, other
than a smaller number of instrumented and fuzzed kernels.

A.3

to 40GB disk space]: Run IvySyn and a selected variant of the Atheris fuzzer, and compare their efficiency
at uncovering crashing inputs.
Preparation: We provide a separate Docker image that
sets-up the two variants of Atheris, namely Atheris+
and Atheris++, which are described in Section 7.1 of
our paper. Similarly to the IvySyn image, you can build

to 15GB disk space]: Run IvySyn and DocTer and
compare their effectiveness at producing PoVs.
Preparation: We provide a separate Docker image that
sets-up DocTer. Similarly to the IvySyn image, you can
either build it from scratch, by running:
comparisons/docter_comp/docker_env/docker

```


## usenixsec2023-final43 — autofz: Automated Fuzzer Composition at Runtime
- artifact: https://github.com/sslab-gatech/autofz/tree/b9a795dda252aa37406d593434b710b0fbedd177
- ref: commit b9a795dda252aa37406d593434b710b0fbedd177
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/fuyufu

```
ad new fuzzer or a new benchmark to autofz).

A.2

Description & Requirements


benchmarks.
3. A VM image which includes all the necessary changes
to the host environment and can be used to launch the
aforementioned docker image.
A.2.1


RAM, and 512 GB SSD disk space. To use the provided
docker image or VM image, 30 GB disk space is required.

Security, privacy, and ethical concerns

A.2.4

Software dependencies

To use the docker image, a working Docker/Podman under
Linux is required. Alternatively, to use the VM image, VirtualBox/VMware is required.
A.2.5


Benchmarks

All benchmarks required for evaluation are already in the
docker image.

A.3

benchmarks will takes a lot of time and resource. Therefore,
we recommend using either the pre-built docker image or the
VM image (preferred).
A.3.1

cgroup v2 downgrade

Hardware dependencies

During the evaluation, we use a cluster of Ubuntu 20.04 machines equipped with AMD Ryzen 9 3900 (12C/24T), 32 GB

Basic Test


benchmark programs for 10 repetitions for Figure 7 in
the paper.
Execution: To run autofz-10 on a target (e.g. exiv2),
use the following command:
autofz -o output-exiv2-autofz10 -t
exiv2 -T 24h -f all -j10 --parallel

of autofz and individual fuzzers on 12 benchmark programs for 10 repetitions for Figure 3 in the paper.
How to: Use autofz with different command line arguments to run all the fuzzing. README.md in the repository has more information about the arguments.
Execution: To run autofz on a target (e.g. exiv2), use
the following command:
```


## usenixsec2023-final55 — Greenhouse: Single-Service Rehosting of Linux-Based Firmware Binaries 
- artifact: https://doi.org/10.5281/zenodo.8217895
- ref: doi 10.5281/zenodo.8217895
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/tay

```
Description & Requirements

Greenhouse was evaluated using a kubernetes cluster containing 42 nodes and over 2,000 CPU cores in order to complete
our analysis on 7,140 firmware images. The Docker image
packaged in this artifact contains an entrypoint script that the
cluster pods use to run Greenhouse on each firmware target.

Hardware dependencies

Greenhouse requires at least 1 CPU core and 8GB of RAM.
As the amount of storage needed varies based on the firmware
and scale of the job, we recommend having at least 50GB of
disk space available. Our full dataset of all 7,140 firmware

images requires at least 125GB of disk space. The total disk
space of our experiment, including all rehosted images and
log files, is approximately 655GB. To perform large-scale
evaluation of Greenhouse, a kubernetes cluster is necessary.
Running on a local minikube instance is possible, but is unstable compared to kubernetes and may have reduced rehosting
performance.

Software dependencies

<container-

• Inside the Docker container, run the setup script:
Greenhouse was tested on a host machine using Ubuntu

third-party software needed for it to run. The artifact Docker
image provided must be run in privileged mode for optimal
results. It is recommended that the host machine be running
Ubuntu 20.04 or later, and have Docker and docker-compose
installed.
A.2.5

Benchmarks

Greenhouse was run on a dataset of 7,140 firmware images
crawled from nine different vendors. This dataset is hosted
privately as part of our artifact submission. Please contact the
authors for access to the dataset if necessary.

```


## usenixsec2023-final60 — EnigMap: External-Memory Oblivious Map for Secure Enclaves
- artifact: https://github.com/odslib/EnigMap/tree/usenix-artifacts
- ref: tag usenix-artifacts
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/tinoco

```
signal-ht code we used to benchmark signal original code. We
provide all our experiment code as single line commands to
make results simpler to reproduce, and the commands should
be simple to modify to try new sets of experimental parameters. We also provide a section explaining at a high level
how our implementation works. Our main goal with the experiments is not to reproduce the exact same numbers as we
have in our graphs, as it will vary greatly with hardware used,

Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

In terms of infrastructure we require 3 types of machines to
reproduce our code. Machine A is used mostly for benchmarking SGX, machine B is used to generate a single graph in our
experiments, machine C is where most of our experiments
were run.

is used mostly for benchmarking ocalls.
(Machine C) - CPU with SGXv2, configured with 192GB
EPC, at least 256GB RAM and and SSD available for
storage. This is used for most of the experiments. We
have a server available with 512GB max EPC and 1TB
RAM that can be used to reproduce the experiments for

Software dependencies

Our artifacts are meant to be run under docker, we provide
the image use to build and run them under tools/docker/buildDockerImage.sh . Alternatively, we also provide a script to
setup a vanila ubuntu 22.04 install (tools/docker/setup_sgx.sh)
to run the artifacts.

Benchmarks

We ran baseline benchmarks on private contact discovery
using signal and signal-ht (signal-icelake) code. We included
them in our repo.


. / benchmark_sgx . e l f
make c l e a n
SGX_MODE=HW SGX_PRERELEASE=1 make
. / benchmark_sgx . e l f

A.4

experiments (using the suggested hardware/software configuration above). Follows an example: Most of our experiments
are run accross exponentially increasing database sizes from a
few bytes to 1TB in size. We include both the time it takes to
run the experiments to reach the main conclusions above, as
well as the time to fully reproduce the graphs in our paper. We
also include the machines required to run each experiment.

(E1.1): [Benchmark SGX] [20 human minutes + 15 computeminutes] [Machine A or B or C] The main goal of this
experiment is to show the costs of ocall and and EWB
in our paper. We defer computing the cost of EWB to
experiment E1.2, altough we analyse it here for clarity.
```


## usenixsec2023-final66 — Automated Analysis of Protocols that use Authenticated Encryption: How
- artifact: https://github.com/AutomatedAnalysisOf/AEADProtocols/tree/V1
- ref: tag V1
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/cremers-protocols

```
the necessary software is made available for easy setup and
execution.

A.2.3

Hardware dependencies

Our artifact does not require any specific hardware. However,
as the used software (e.g. the Tamarin Prover 1 ) does also
scale with computation power and memory, we recommend to
at least use a modern notebook or similar modern computing
devices. GPUs are not required.
A.2.4

Software dependencies

We provide access to a docker2 image which has all the necessary software dependencies pre-installed.
(Optional) Dependencies for manual installation In case
the reviewers choose to manually install the dependencies,
they should install the following

Benchmarks

None.

A.2


Description & Requirements

A.3

Set-up


missing Haskell dependencies or outdated versions of
Maude
- Make sure that the tamarin-prover executable is in the
$PATH.
A.3.2


```


## usenixsec2023-final84 — GigaDORAM: Breaking the Billion Address Barrier
- artifact: https://github.com/jacob14916/GigaDORAM-USENIX23-Artifact
- ref:  
- paper: https://www.usenix.org/conference/usenixsecurity23/presentation/falk

```
processes via the tc command and benchmark the performance of GigaDORAM in a variety network settings.

Abstract

• Multi machine tests: we execute GigaDORAM on 3
different AWS EC2 instances in the same AWS region.

The repository contains a C++ implementation of the GigaDORAM protocol, benchmarking scripts, and explanations
helpful to reproducing the experiments in the paper. The explanations are composed of a standard README file and a
detailed video walkthrough which we believe to be the most
convenient way to install GigaDORAM and reproduce our
results.


Hardware dependencies

For evaluation, a processor supporting the Intel SSE2 instruction set is and we recommend at least 8 CPU cores and 8GB
of RAM. While local evaluation of our artifact is possible,
benchmarking on AWS is necessary for replicating our results.
If AWS credits are not available to reviewers, please reach

Description & Requirements

Roughly speaking, we benchmarked GigaDORAM in 2 different settings

A.2.4


Software dependencies

• A Linux machine with processor supporting the Intel
SSE2 instruction set.

• Single machine tests: we execute GigaDORAM through

and its dependencies.

• In addition to the requirements for single server tests, the
AWS CLI (package awscli in apt) needs to be installed
on the machine used for builds.


– EMP’s dependencies are extremely basic (python3
cmake git build-essential libssl-dev)
and are all needed to build GigaDORAM. Those
can be installed using the apt package manager.

• After installing, configure your region and access keys

• On a typical Linux system there are no dependencies
needed to run the compiled binary.
A.2.5

Without disabling StrictHostKeyChecking, the experiment script will be unable to ssh to new hosts in the
background, since user input would be required to continue connecting to a new host.

Benchmarks

No data is needed to run our tests.

```


## usenixsec2024-final10 — CAMP: Compiler and Allocator-based Heap Memory Protection
- artifact: https://github.com/cla7aye15I4nd/CAMP/tree/a74a3069adb4aeff2426bba1fd6391c7d1fbb405
- ref: commit a74a3069adb4aeff2426bba1fd6391c7d1fbb405
- paper: https://www.usenix.org/conference/usenixsecurity24/presentation/lin

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Software dependencies

• Docker

Abstract


benchmarks.
This artifact is seeking the Artifacts Available badge, the
Artifacts Functional badge, and the Results Reproduced
badge. To facilitate the artifact evaluation, we have provided
multiple Docker environments. The Docker environments
are designed to reproduce the evaluation results of CAMP,

Benchmarks

It’s preferable to utilize the SPEC CPU2016 and SPEC
CPU2017 benchmarks. With them, you can manually employ
CAMP for compilation. However, if you don’t possess these
benchmarks, you can alternatively make use of our Docker.

Hardware dependencies

• Processor: We recommend using a 12th Gen Intel i712700 CPU with a clock speed of 4.9 GHz to achieve
results similar to our experiments. However, comparable
hardware may also suffice.


(C1): CAMP achieves good performance and memory overhead with the SPEC benchmark and is capable of handling real-world programs. This is substantiated by experiments (E2), (E3), and (E4).
(C2): CAMP able detect all memory corruption in juliet and
CVE benchmarks which mentioned in our paper. This is
proven by the experiments (E1) and (E5).
A.4.2


(E4): Performance Evaluation on SPEC Benchmark The
environment is contained within the Docker image
dataisland/camp-spec. To run the test, use the command provided below. You will be able to see the time
and memory consuming of each testcases.



(E5): Security Evaluation on CVE Benchmark
How to: Download and create container n7l8m4/*
Preparation: None.
Execution: In every container, we have set up test.sh,
test_OOB.sh, test_UAF.sh, in /root directory. Test
can run the test.sh to automatically run the test cases.

```


## usenixsec2024-final22 — NetShaper: A Differentially Private Network Side-Channel Mitigation Sy
- artifact: https://github.com/ubc-systopia/netshaper/tree/AE_v2.0
- ref: tag AE_v2.0
- paper: https://www.usenix.org/conference/usenixsecurity24/presentation/sabzi

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

The simulator requires a machine that should have at least 8
CPU cores, 64 GB of RAM, and a GPU with 24 GB of memory. To store the dataset and experiment results, simulator
needs 100 GB of disk space. For NetShaper implementation,
we use four machines interconnected in a linear topology.

RAM, 100 GB of disk space, and a 10 Gbps NIC. The machines should be connected to a LAN, ensuring no interference from the public network or other network applications.
A.2.4

Software dependencies

Simulator requires Python 3.10.6 and can be executed on

our modified version of wrk2, an HTTP benchmarking tool,
to send requests asynchronously. The list of main software
dependencies are provided in Git repository.

How to access


Benchmarks

• Datasets: We use two datasets, one for our video streaming service and another for our web service. Instructions
for accessing these datasets can be found in Section
A.2.2.
• Models: We use TCN model and CNN model from the

pip install -r <path-to-simulator>/requirements.txt

A.3.3

Basic Test


imposed by NetShaper middleboxes. This experiment is located in the ’microbenchmarks’ directory
in the project’s repository.
(E3): (Video Streaming Latency Overhead)[30 humanminutes + 4 compute-hours]: This experiment evaluates the latency of video streaming application with
NetShaper traffic shaping.
(E4): (Video Streaming Bandwidth Overhead)[5 humanminutes + 3 compute-hours]: Measuring the bandwidth overhead of the video streaming application
with NetShaper traffic shaping.

```


## usenixsec2024-final33 — Operation Mango: Scalable Discovery of Taint-Style Vulnerabilities in 
- artifact: https://github.com/sefcom/operation-mango-public/tree/ff15727d3d9f7016e91e3f07a983e81090a62b3d
- ref: commit ff15727d3d9f7016e91e3f07a983e81090a62b3d
- paper: https://www.usenix.org/conference/usenixsecurity24/presentation/gibbs

```
Description & Requirements

Mango can be run parallelized locally with the use of docker
containers or with Kubernetes remotely. However, we will
not give any support for running on Kubernetes, nor can we
provide access to our computing resources. Mango will spit

Hardware dependencies

There are no specific hardware dependencies, but we suggest
a sufficiently powerful machine to run the experiments. Our
experiments were run on a Kubernetes cluster with access to
4000 cores. We also require at least 500GB of storage if you

up to 400GB of disk space.
A.2.4

Software dependencies

Our artifact is consolidated into two Python packages, which

Benchmarks

Here are all of the datasets we used.
karonte dataset: https://drive.google.com/file/
d/1-VOf-tEpu4LIgyDyZr7bBZCDK-K2DHaj/view?usp=
sharing

```


## usenixsec2024-final81 — Automated Large-Scale Analysis of Cookie Notice Compliance
- artifact: https://github.com/bouhoula/alsacnc/releases/tag/v1.0.3
- ref: tag v1.0.3
- paper: https://www.usenix.org/conference/usenixsecurity24/presentation/bouhoula

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Software dependencies

The artifact requires Docker and Docker Compose. As for the
host machine, we tested various Linux distributions without
issues.
The crawler uses the ports 5000, 5001, and 5432.

Benchmarks

Benchmarks do not apply to our artifact. However, the machine learning models are trained on the following datasets:
• A dataset of 400 cookie notices annotated by Santos et
al. [45]. This dataset is not included as it is not public.
However, it is available upon request by contacting the

Hardware dependencies

The artifact can run on any machine with an x86-64 architecture CPU and the necessary software dependencies. We used
a machine with a 16-core CPU (AMD 5950X), 64GB RAM,
and an RTX 3080 Ti GPU. Machines with different performance may require to adjust the --num_browsers parameter,
which indicates the number of parallel browsers used by the

```


## usenixsec2025-final38 — Atkscopes: Multiresolution Adversarial Perturbation as a Unified Attac
- artifact: https://zenodo.org/records/15114114
- ref:  
- paper: 

```
Description & Requirements

The attack against PhotoDNA has been tested on a 64-bit Windows machine. This limitation is due to the PhotoDNA binary,
which is architecture-specific. The attacks on phash, PDQ, and
NeuralHash have been tested on Linux. It is important to note
that the attack on NeuralHash requires a CUDA-supported

Hardware dependencies

The only dependency is the need for a machine compatible
with the corresponding .dll or .so file. This should work in a
64-bit Windows environment.
A.2.4

Software dependencies

The main dependencies are Docker, TensorFlow, and PyTorch.
Other dependencies are listed in the requirements.txt.
A.2.5


Benchmarks

In the artifact, we provide executable Python files for escaping and triggering regulation attacks on pHash, PDQ, PhotoDNA, and NeuralHash. We evaluate our two attack scenarios using the ImageNet dataset from the ILSVRC 2012
challenge. For our experiments, we have randomly selected
50 pairs of images from the ImageNet dataset, which are
available in the directories ./imagenet_50_resized/ and

$ pip install -r requirements . txt

For running files under AtkScope_NeuralHash, we recommend configuring the environment on a Linux system. Please
run the following command from the project’s root

$ python adv1_target_attack . py -- source =

```


## usenixsec2025-final48 — Flexway O-Sort: Enclave-Friendly and Optimal Oblivious Sorting
- artifact: https://zenodo.org/records/14629454
- ref:  
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


greatly with hardware used, but to show that the speedup we
obtain, as well as the assymptotic behavior is similar to the
shown in our paper.

A.2.2


Hardware dependencies

In terms of infrastructure all of our experiments were run on
the same machine, with the following specifications:

• 1TB DDR4 RAM, 512GB of maximum EPC size.

Software dependencies

Our artifacts are meant to be run under docker, please see the
installation steps in order to know how to build and launch
the docker container.
A.2.5

Benchmarks

We ran artificial benchmarks on sorting arbitrary arrays comparing with several sorting implementations. And on generating a histogram, initializing an ORAM and load balancing,
comparing Flexway O-Sort with bitonic sort.

A.3

(C1): Flexway O-Sort is an assymptotically optimal and concretely efficient sorting algorithm suitable for implementation in hardware enclaves such as Intel SGX having
speedups when compared to other state of the art oblivious sorting algorithms for enclaves.
(E1a) and (E1b) show the speedup of Flexway O-Sort
against other oblivious sorting algorithms in an enclave
setting, supporting the claim (C1).
(C2): Flexway O-Sort is also optimal when the input size is

(E3a): [Application Benchmarks, EPC < data] [15 humanminutes + 3 compute-hour]: Table 3 (128MB EPC)
How to: Change the parameters in algo_runner.sh to
match the ones for Table 3: Benchmark Results for Different Applications. Run the script. Collect the speedup
between running the application with Flexway O-Sort
and the optimized recursive bitonic sorter in a table similar to Table 3 in our paper.
Preparation: Do the initial setup.

to match the ones for Table 3: Benchmark Results for
Different Applications. Run the script. Collect the points
in a table and see that there is always a speedup when
using Flexway O-Sort instead of the bitonic sorter.
The script will generate a file in the same format as in
E1a. Each benchmark type will have a different format,

(E3b): [Application Benchmarks, EPC > data] [15 humanminutes + 3 compute-hour]: Table 3 (EPC > data)
How to: Build the project as in (T1) and run the binary
in ./build/tests/test_apps. The tests will output the runtime for baseline and our as can be seen in table 3.

```


## usenixsec2025-final138 — Oblivious Digital Tokens
- artifact: https://zenodo.org/records/14737533?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjQxYTgyZWU2LTk1YWEtNGEzOS05MjM1LWM0NzYwZjY1ZmFjNiIsImRhdGEiOnt9LCJyYW5kb20iOiI5MDBlMjg0OTg2NGJhOGVkNzE4NzBmZTU5YTRhOTM3YyJ9.h8Z2HxamuZDdBiTIVuEy1U-g4ef0S8nAOikKMxm_XSspAQ-h7fMpoE-ZxCJ0IIF-oDX7IIKPRPs77dvPlwPGjg
- ref:  
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

Artifact (A1) does not require special hardware and the complete proof can be computed and inspected on commodity
hardware with 8 GB of RAM and 10 GB of swap space. It
takes up to 30 minutes to compute the proof and up to 30 minutes to open it for inspection, with an Intel(R) Core(TM)
1 https://github.com/Anonymous-Usenix-25/ObliviousDigital-Tokens/releases/tag/usenix

Software dependencies

Artifact (A1) requires the Tamarin prover, which is available
for MacOS, Linux, and Windows.
Artifact (A2) is developed for Linux. It requires the Intel
SGX SDK driver, Intel SGX SDK library, Intel SGX PSW library, the Intel SGX SSL library, and an OpenSSL installation.

the Intel SGX SDK driver. For the rest of the dependencies,
we provide a script that allows a user to interactively install
them, and a Docker image (and corresponding Dockerfile)
where the dependencies are installed automatically. For both
options, the dependencies are fixed to specific versions and
should continue to install and work in the future. Note that

Benchmarks

None.

A.3


that evaluators update their kernel if possible. For hardware
that supports only SGX1, the kernel driver seems to not work,
so one must manually install the older driver according to the
instructions found at: https://github.com/intel/linuxsgx-driver. For the remaining installation steps, we provide
a setup.sh script in the scripts directory of artifact (A2)
that performs the installation process. The installation process takes around 90 minutes on our hardware and asks for

```


## usenixsec2025-final171 — Tracking You from a Thousand Miles Away! Turning a Bluetooth Device in
- artifact: https://doi.org/10.5281/zenodo.14728530
- ref: doi 10.5281/zenodo.14728530
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Table 1: Hardware configurations used for each component
Component

Hardware Requirement

C&C Server

Hardware dependencies

Table 1 details the hardware configuration in our experiment.
1 https://doi.org/10.5281/zenodo.14728530
2 https://nroottag.github.io/


Table 2: Software configurations used for each component

A.2.4

Component


Software Requirement

C&C Server
Key Seeker
Trojan - Linux
Trojan - Android

Software dependencies

Table 2 shows the software setup, which is the same as the
software environment used in the demonstration videos.
If evaluators have further requirements for confirming the
submission and decryption of location reports, evaluators may

Benchmarks

None, our work does not compare with other datasets.

A.3


# Method A, install from requirements
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# OR, Method B, use our packed venv
tar xvf venv.tgz

(E1): [Key Seeker Benchmark] [0.5 human-hour]
Preparation: In this experiment, the Key Seeker is evaluated for correspondence to C1.
Execution: Navigate to nRootTag/executables and run
the following commands. In the given example code, -t 0
```


## usenixsec2025-final206 — Surviving in Dark Forest: Towards Evading the Attacks from Front-Runni
- artifact: https://zenodo.org/records/14735789
- ref:  
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

None.
A.2.4

Software dependencies

all software dependencies.
A.2.5

Benchmarks

The

```


## usenixsec2025-final32 — From Constraints to Cracks: Constraint Semantic Inconsistencies as Vul
- artifact: https://doi.org/10.5281/zenodo.15605329
- ref: doi 10.5281/zenodo.15605329
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

Our evaluation of N ÜWA was conducted on a host machine
with a 28-core Intel Xeon processor and 256 GB of RAM
running Ubuntu 22.04. However, N ÜWA does not require any
specific hardware features and can run on any Linux-based

operating system. No specialized hardware (e.g., GPU, FPGA,
or hardware counters) is needed. Higher-end configurations
may improve performance, but they are not mandatory for
functionality. We recommend at least 8 CPU cores and 32 GB
of RAM for smooth execution and reasonable analysis time.
N ÜWA can also be executed within a virtual machine environment and does not require root privileges for installation

Software dependencies

To evaluate N ÜWA, the most critical requirement is the installation of IDA Pro (version 9.0 or 9.1) with full decompiler
plugin support. Since IDA Pro is a commercial reverse engineering software, we are unable to provide a pre-configured



license and install the software independently.
In addition, N ÜWA was evaluated using Python version
3.10.12, and we strongly recommend using the same version
to ensure compatibility and reproducibility.
A.2.5


Benchmarks

We used two datasets to evaluate N ÜWA. The first is a knownvulnerability dataset, included in the vuln_dataset folder,
which consists of firmware samples containing vulnerabilities with publicly available ground truth. The second is a
firmware dataset used for discovering previously unknown
vulnerabilities, included in the firmware_dataset folder. Due

As described in Section A.2.4, to download and install dependencies as well as the main artifact, you only need to install
IDA Pro (version 9.0 or 9.1) and Python (version 3.10.12 is
recommended).
Then, follow the instructions provided in our Zenodo repository to configure the Python virtual environment.
Or you can use N ÜWA in the Docker provided in our Zenodo repository, which only you need to install IDA Pro and
configure IDALib.

```


## usenixsec2025-final75 — Beyond Exploit Scanning: A Functional Change-Driven Approach to Remote
- artifact: https://doi.org/10.5281/zenodo.15576928
- ref: doi 10.5281/zenodo.15576928
- paper: 

```
Remote Software Version Identification
Jinsong Chen†* , Mengying Wu†* , Geng Hong†* , Baichao An† , Mingxuan Liu‡ , Lei Zhang† , Baojun Liu§ ,
Haixin Duan§¶ and Min Yang†
† Fudan University, {jschen23, wumy21}@m.fudan.edu.cn, {ghong, bcan20, zxl, m_yang}@fudan.edu.cn
‡ Zhongguancun Laboratory, liumx@mail.zgclab.edu.cn
§ Tsinghua University, {lbj, duanhx}@tsinghua.edu.cn

In this paper, we present VersionSeek, a new functionalitybased tool for software version identification through functional probe generation and automated response analysis. It
includes the source code for software deployment, functional
probe generation, response processing, and version identification. The artifact also contains ethically filtered and validated
probes along with their corresponding locally generated response outputs. In addition, it provides the source code and
training data used to construct the comparative baseline. A
comprehensive README file is included to facilitate the

software systems. Additionally, validation experiments are included to demonstrate the effectiveness of these capabilities.

A.2

Description & Requirements


specify the required hardware and software environments.
Our artifact consists of seven main folders: Deployment, Generation, ResponseProcessing, VersionIdentification,
Probes, ProbeOutputs, and Comparison. The Deployment
folder contains automated deployment code for five opensource software systems. The Generation folder includes code for automatically generating functional probes
using large language models (LLMs), guided by functional changes and their corresponding contextual information. The ResponseProcessing folder implements response standardization and classification modules. The
1 These authors contributed equally to this work.

identification modules tailored to the selected software targets.
The Probes and ProbeOutputs folders contain ethically filtered and validated functional probes, along with their locally
generated response outputs. Finally, the Comparison folder
provides baseline implementations and training data for various machine learning and black-box approaches used in our
comparative evaluation.
A.2.1

Hardware dependencies

We implemented this artifact on a server with a 13th Gen
Intel® Core™ i7-13700 processor (24 cores), 32GB of memory, and a 1TB SSD. Additionally, the LLM used in our experiments, Qwen2.5-32B-Instruct, was deployed on a server
equipped with an Intel® Xeon® Gold 6330 CPU @ 2.00GHz


Software dependencies

Although our experiments were conducted primarily on
Ubuntu 23.04, the artifact is compatible with any Linux-based
environment that supports Python 3.11. However, we recommend using Ubuntu 22.04 or Ubuntu 24.04 for better stability. We use Miniconda for environment and dependency
management, and all required packages are specified in the

requirements.txt file located at the root of the repository.
A.2.5

Benchmarks

A.3.2

system commands and Python dependencies are properly
installed:
python versionSeek.py --test
Upon successful verification, the output will be: All required
```


## usenixsec2025-final82 — Private Investigator: Extracting Personally Identifiable Information f
- artifact: https://doi.org/10.5281/zenodo.16748364
- ref: doi 10.5281/zenodo.16748364
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Software dependencies

Private Investigator requires CUDA 12.1 and Python
3.10, along with the following Python libraries: Pytorch
2.1.2, Transformers 4.51.3, and Flair (https://github.
com/flairNLP/flair).

Instructions for downloading the required software,
datasets, and model weights are provided in § A.3.1.
A.2.5

Benchmarks


Hardware dependencies

Private Investigator requires a Linux machine with an
NVIDIA graphics card. Due to the large size of LMs and
datasets, we recommend using a machine with at least 32
CPU cores, 128 GB of system memory, 24 GB of GPU memory, and 150 GB of disk space. We tested the Docker image

To verify that all required software dependencies are properly
installed, run basic_test.py located in the experiments/
directory. This script specifically tests the TREC dataset and
evaluates its perplexity on the OpenELM model fine-tuned on
that dataset. If everything is set up correctly, it should print a
perplexity value of 3.6.

```


## usenixsec2025-final89 — Hercules Droidot and the murder on the JNI Express
- artifact: https://doi.org/10.5281/zenodo.15586319
- ref: doi 10.5281/zenodo.15586319
- paper: 

```
gives a brief overview of the resource requirements to replicate some of the experiments conducted in our evaluation,
along with instructions to run them.

A.2

Description & Requirements

Hardware dependencies

Our evaluation requires Android emulators to run the mobile
applications under test. Modern Android emulators require
ARM64 architecture for optimal performance and compatibility with contemporary Android versions.
To accommodate reviewers during the artifact evaluation

This server enables reviewers to reproduce our experimental results without requiring them to have ARM64 hardware
locally. However, we note that those servers have more limited computational resources compared to the AWS cluster
infrastructure used in our original paper evaluation.
The difference in computational resources between the
evaluation servers and our original experimental setup should
not affect any of the major claims made in our paper.

Software dependencies

All software dependencies are managed through our Docker
container.
The Docker container ensures reproducible builds and eliminates dependency conflicts across different host systems. No
additional software installation is required on the host machine beyond Docker itself.

Benchmarks

As outlined in the paper, there are no clear benchmarks defined by literature to evaluate Android native library fuzzers.
Therefore, included in the artifact we ship the most 100
popular Android applications. They can be found in the
target_APK folder.

4. Run ./setup.sh to download dependencies and build
the Docker container.
5. Spawn a shell in the container: ./run.sh.
x86 Server for Static Analysis Tools:
1. Login
to

5. Run ./setup.sh to download dependencies and build
the Docker container.
6. Run ./build_docker.sh to download dependencies
and build the Docker container.
7. Spawn a shell in the container: ./start_docker.sh.
A.3.2

```


## usenixsec2025-final96 — Ares: Comprehensive Path Hijacking Detection via Routing Tree
- artifact: https://doi.org/10.5281/zenodo.15589806
- ref: doi 10.5281/zenodo.15589806
- paper: 

```
Description & Requirements

Since our artifacts include not only the source code of Ares
but also the code for three other methods (Metis, DFOH, and
BEAM), we will separately specify the dependencies required
for each of the four approaches.

Hardware dependencies

Our experiment was conducted on a server with Intel(R)
Xeon(R) Gold 5218R CPU@2.10GHz which has 80 cores.
To successfully run Ares, you will need a server with sufficient memory (better over 100GB, our experimental machine
was equipped with 251GB RAM). Furthermore, to properly

three methods involve machine learning components. Moreover, you will need over 166GB disk space to store DFOH’s
database.
A.2.4

Software dependencies


Ares. To successfully run Ares, you need to install the dependencies listed in the README document, which include:
Python dependencies specified in requirements.txt, The bgpdump toolkit, The BGPStream framework. The README
provides direct links to installation instructions for these components. Additionally, to mitigate potential dependency conflicts (e.g., from pre-existing packages in the server environ-


ment prior to experimentation), we provide a requirementsfull.txt file containing all explicitly tested package versions.

Python dependencies listed in requirements file in its folder.
BEAM. To compare BEAM with Ares, you need to follow
the instructions listed in its original readme document at
’BEAM/readme.md’ to install dependencies.
DFOH. To compare DFOH with Ares, you will need to install
Docker and Python dependencies. Instructions are included

Benchmarks

Ares. The data required by Ares in the experiments with this
artifact are already documented in the ’Data’ folder.
Metis. The data and model required by Metis in the experiments with this artifact are already documented in the ’Metis’
folder and some of its sub-folders.

/README.md. To install dependencies, follow the instructions
bellow:
1. Install bgpdump tool following instructions at https://gi
thub.com/RIPE-NCC/bgpdump/wiki. Note to add this tool
to the system PATH.
2. Install libBGPStream following instructions at https:

3. Install Python dependencies using pip install -r
requirements.txt.
This should lead you to run Ares. If there are any missing
dependencies, you could supplement it or check requiremen
ts-full.txt.
Metis. Instructions are included in readme document at Me

tis/README.md. Install Python dependencies using pip
install -r requirements.
BEAM. Original instructions are included in readme document at BEAM/readme.md and our instructions are at
BEAM/README.md. Follow the original instructions to install dependencies. Note that if you want to use the model
```


## usenixsec2025-final124 — GDMA: Fully Automated DMA Rehosting via Iterative Type Overlays
- artifact: https://doi.org/10.5281/zenodo.15600641
- ref: doi 10.5281/zenodo.15600641
- paper: 

```
Description & Requirements

This artifact is a fuzzing artifact and hence scales better the
more resources it can use. In our setup, we ran each experiment 10 times, 24 hours each. We used two Intel Xeon Gold
5320 CPUs (26 physical cores and 2.20GHz each), 256 GB
of RAM, and 1TB SSD storage.

even on moderate hardware, the artifact evaluation time period
suffices. With this configuration, one full pipeline run takes
eleven days. Please take this into account when inspecting this
artifact. However, it is possible to split up the long-running
parts over several machines to reduce runtime.


The minimal requirements are 26 cores, 64GB RAM and
500GB disk storage. More cores can speed up the experiments,
as can multiple machines.
A.2.5

A.2.1

Requirements

Hardware Dependencies

Software Dependencies


Please install the following software dependencies:

All experiments were run on an Ubuntu 22.04 machine. We
provide reduced fuzzing configurations to account for artifact reviewers without access to hardware clusters. However,
our recommended configuration still requires eleven days of
computing on a single piece of minimal hardware. Therefore,

Benchmarks

Setup

The setup is tested on Ubuntu 22.04.
1 https://docs.docker.com/engine/install/linux-postinstall/

Enter the scripts directory and install the requirements in a
clean virtual environment.

A.4

Evaluation Workflow

pip install -r requirements.txt

We expect all further commands to be executed from
within the virtual environment. To finish the installation of
the GDMA experiments artifact, move the three remaining
archives (A3-A5) to their place as described below.

hours + 45GB disk space (if docker export or import is
used), O1)
(E2): Example applications reproduction: rebuild the example applications from its sources (10 human minutes
+ 0.5 CPU hours + 45GB disk space (if docker export or
```


## usenixsec2025-final126 — SoK: Automated TTP Extraction from CTI Reports – Are We There Yet?
- artifact: https://zenodo.org/records/15608555
- ref:  
- paper: 

```
Description & Requirements

This artifact has been executed on a server mounting two
NVIDIA L40 GPUs with 48GB VRAM, 1024GB RAM,
and two AMD EPYC 7763 CPUs. The server runs Ubuntu
22.04.04 (jammy), with CUDA version 12.4.

Hardware dependencies

We recommend having at least 48GB of GPU VRAM and
300GB of storage.
A.2.4


Software dependencies

Our artifact partly depends on the DarkBERT3 model, which
requires an access token key by contacting the authors of the
paper to be downloaded.
A.2.5

Benchmarks

Our artifacts require the following datasets: TRAM2, and
AnnoCTR. Both are provided directly in our repository, in the
dataset folder.


with the transformers8 library version 4.44.2. Unfortunately, we could no longer reproduce this combination of dependencies, which is why we switched to the newer versions
unsloth==2025.03.19 and transformers==4.51.1. This
results in the behavior as described in chapter 6.2 - Prompt
based, that the LLM suffers from instability and sometimes
gets into a loop in which all MITRE IDs are output, which
increases the recall, but reduces the precision and accordingly

```


## usenixsec2025-final138 — TRex: Practical Type Reconstruction for Binary Code
- artifact: https://doi.org/10.5281/zenodo.15611994
- ref: doi 10.5281/zenodo.15611994
- paper: 

```
producing reproducible benchmark binaries, as well as the
scripts needed to run the evaluation presented in §5 of the
main paper.

A.2


Description & Requirements

A.2.1

Security, privacy, and ethical concerns


This artifact includes (i) the source code for TRex, (ii) reproducible scripts for the benchmarks, and (iii) evaluation
framework to reproduce the results in §5 of the paper.
The artifact is archived at https://doi.org/10.5281/
zenodo.15611994. Within this artifact, the TRex tool itself sits within trex/, the benchmark scripts sit within
trex-usenix25/benchmarks/, and the rest of the files in
trex-usenix25/ are the evaluation scripts/framework.

trex-usenix25 for the evaluation and benchmarks. The
artifact contains a symlink from trex-usenix25/trex to
../trex to establish the directory structure expected by our
evaluation framework.

Details of software requirements, instructions, and more

Hardware dependencies

No special hardware is needed for running TRex, or indeed
most of the evaluation, and a regular commodity x86-64 system suffices. While TRex itself works on ARM-based devices
too, building the benchmark binaries requires an x86-64 machine. For future reference, we note that we ran our evaluation
on a server with an Intel i9-10980XE (with 36 logical cores)

can be run using lower hardware specifications at the cost of
a longer run time.
For replicating §5.3 in particular (i.e., evaluation against
the Machine Learning-based prior work called ReSym), we
recommend using a system with sufficiently powerful GPU
(with CUDA support). The ReSym paper itself uses four

Software dependencies

The evaluation has a small number of software dependencies
that we list in the relevant READMEs. In short, we require
an installation of Rust, Just, Python, uv, rename, and Ghidra.
We have tested the evaluation locally on both Ubuntu 22.04

Benchmarks

Benchmark binaries for the evaluation consist of C OREUTILS
and S PEC. For the former, no special access other than internet is needed, and the reproducible scripts will automatically download and build the binaries after confirming a



Our reproducible scripts will confirm its cryptographic checksum and then use it for compiling the benchmark binaries.

A.3

```


## usenixsec2025-final143 — Aion: Robust and Efficient Multi-Round Single-Mask Secure Aggregation 
- artifact: https://doi.org/10.5281/zenodo.15605465
- ref: doi 10.5281/zenodo.15605465
- paper: 

```
♮ Institute of Software, Chinese Academy of Sciences

Email: {liuyizhong, jiazixiao, jinzian, chenxiao, sbian, runhua, lidawei, liujianwei}@buaa.edu.cn, luyuan@iscas.ac.cn

A


Description & Requirements

This section details the experimental setup, specifying the
hardware and software environments, as well as the benchmarks employed to generate the reported results.
A.2.1


Software dependencies

E1 is compatible with both Windows and Linux, except for
the ACORN scheme, which is only supported on Linux. E2 is
compatible with Windows, while E3 is for Linux. We strongly
recommend deploying E2 and E3 using Docker, which is

compatible with both Windows and Linux. All required dependencies are listed in the requirements.txt.
A.2.5

Benchmarks

Our experiments require the CIFAR10, FMNIST, EMNISTByclass, and SHAKESPEARE datasets, which are automatically downloaded from their official sources during code

-r requirements.txt
We recommend using Docker for installation of E2 and E3.
The pre-built images can be downloaded as follows:
E2: docker pull aionaion/input_validation:latest
E3: docker pull aionaion/gradattack:latest


Hardware dependencies

Evaluating our artifact requires a system equipped with at least
an NVIDIA GeForce RTX 3060 GPU and with no specific
CPU requirements. However, for efficiency, we recommend


You can also verify that all required dependencies are correctly installed without using Docker:
E2: python ./FL_Backdoor_CV/roles/autorun.py
E3: python examples/attack_cifar10_
gradinversion.py #remove spaces in file path
For E2, if the training progresses to Round 301, you can
safely terminate the process. For E3, we recommend waiting

```


## usenixsec2025-final156 — Tady: A Neural Disassembler without Structural Constraint Violations
- artifact: https://doi.org/10.5281/zenodo.15541311
- ref: doi 10.5281/zenodo.15541311
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

The experiments were conducted on a machine with the following specifications:
• CPU: Intel Core i9-12900K
• GPU: NVIDIA RTX A6000 Ada generation (A GPU is
required for model training and inference)

Software dependencies

The artifact can be run on host or within a Docker container.
• Operating System: Ubuntu 24.04.
• Core Dependencies:
– C++ toolchain (build-essential)

with all necessary dependencies for Tady.

tar -xzvf bin.tar.gz -C data
tar -xzvf gt_npz.tar.gz -C data
tar -xzvf eval_strip_baselines.tar.gz \
-C data

used if the baseline software itself is not accessible.

At this point, the environment is ready for evaluation.

A.2.5


Benchmarks

The evaluation uses several public and custom datasets, all of
which are provided and can be generated with the artifact’s
scripts. The primary datasets are:
• Pangine: Binaries compiled with various compilers and

• obf-benchmark: 11 binaries obfuscated with binobf.
The artifact provides scripts to download, preprocess, and format these datasets. Pre-processed datasets are also available
for download to expedite evaluation.

A.3


standard and obfuscated benchmarks. This is proven by
experiment (E1), with results in Table 3 of the paper.
(C2): Tady’s post-processing pruning algorithm effectively
eliminates all detected structural constraint violations
from the model’s output, improving consistency while
maintaining or improving F1 score. This is proven by

and dataset labels across all benchmarks.
Preparation: Ensure E1 has been completed and the
intermediate results in data/prune are available. The
errors are already detected in our pruning scripts.
```


## usenixsec2025-final175 — A Crack in the Bark: Leveraging Public Knowledge to Remove Tree-Ring W
- artifact: https://doi.org/10.5281/zenodo.15595719
- ref: doi 10.5281/zenodo.15595719
- paper: 

```
Description & Requirements

no risk associated with the security of the machine or data privacy. With regard to ethical concerns, Tree-Ring watermarking is still in the prototype stage and has not been deployed.
Therefore, the likelihood of malicious actors exploiting these
attacks is minimal, while exposing their vulnerabilities gives
a better understanding of the limitations of ML watermarking.

Hardware dependencies

Our experiments were run on an Nvidia A100 GPU with
80GB of VRAM with 8 CPU cores. The minimum memory
requirement is 32GB with atleast 50GB of storage available.


All software dependencies are listed in the README file
inside the repository. The minimum requirements are Python
and a package manager (e.g. conda/pip/mamba). The Dockerfile also constructs a machine image with the Python environment already setup.

A.2.1


Software dependencies

Benchmarks

The datasets are provided within the Zenodo repository for
this project. The diffusion models such as Stable Diffusion,

README under the section ’Dependencies’. This step can
be skipped if
A.3.2

Basic Test


```


## usenixsec2026-final67 — Trustworthy and Confidential SBOM Exchange
- artifact: 
- ref:  
- paper: 

```
Software Bill of Materials (SBOM) exchange. Petra enables
selective disclosure of SBOM fields using Ciphertext-Policy
Attribute-Based Encryption (CP-ABE) while preserving verifiable integrity through Merkle-authenticated SBOM trees.
The artifact includes: (i) Petra’s implementation, (ii) CP-ABE
bindings, (iii) SBOM preprocessing and evaluation scripts
to reproduce the performance and storage overhead results

Description & Requirements

The artifact evaluates Petra’s ability to securely encrypt, decrypt, and verify redacted SBOMs at scale. Experiments measure: tree construction cost, Merkle hashing cost, encryption
and decryption overhead, storage overhead across plaintext,
encrypted, and decrypted SBOM trees.
The evaluation uses Chainguard’s bom-shelter SBOM

elevated privileges (except installing dependencies), or access
to sensitive personal data. The evaluation processes publicly
available SBOM datasets and locally generated cryptographic
keys. No network services are contacted except for dependency installation and dataset retrieval. The included Key
Management Service (KMS) runs locally for testing purposes
only.

A Docker image containing all required dependencies for
Petra and its evaluation pipeline, can also be rebuilt locally
using the Dockerfile included in the source archive.
A.2.3

Hardware dependencies

and 256 GB of RAM. No specialized hardware (e.g., GPUs,
FPGAs, or hardware accelerators) is required to evaluate this
artifact.
A.2.4

Software dependencies

Python dependencies Installed via pip install -r requirements.txt
Rust dependencies Built via maturin for CP-ABE bindings
A.2.5

Benchmarks


pip install -r requirements.txt

# From artifact root directory(SBOMCtl)
cd privateSBOMExchange
python tests/test_models.py


```


## usenixsec2026-final91 — FIRA: Enabling Automatic Forensic Investigation of Unmanned Aerial Veh
- artifact: https://doi.org/10.5281/zenodo.18395925
- ref: doi 10.5281/zenodo.18395925
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

The experiments require a CUDA-capable GPU for neural
network inference and attribution analysis. Our evaluation
environment uses:
• 1× NVIDIA A6000 GPU (48 GB VRAM)

• about 20 GB disk space
A pre-configured machine with the above hardware is accessible via the SSH.
A.2.4

Software dependencies


Benchmarks

All required data is included in the artifact:

ssh -i /path/to/key -p 10467
usenix_ae@0.tcp.ngrok.io

```


## usenixsec2026-final97 — DMGuard: Safeguarding Kernels from Physical-Page Use-After-Free Vulner
- artifact: https://doi.org/10.5281/zenodo.17970502
- ref: doi 10.5281/zenodo.17970502
- paper: 

```
Note that some tests requiring specific hardware or kernel
versions are excluded from this artifact. Since the performance evaluation runs on QEMU emulation, absolute numbers may differ from those reported in the paper.

A.2

Description & Requirements

Hardware dependencies

The artifact requires an x86_64 host machine. The minimum
requirements are 8GB RAM and 100GB free disk space. We
recommend 16GB RAM and 8+ CPU cores for faster kernel
builds. No special hardware is required as the artifact uses

Software dependencies

The artifact requires Linux with Docker Engine and Docker
Compose installed. All other dependencies are included in the
Docker image and require no additional installation. These
include LLVM-19/Clang for kernel builds, QEMU system

Benchmarks

The CVE PoC code was collected from public GitHub repositories and Project Zero issue tracker. For performance evaluation, we use LMBench microbenchmark, which is publicly
available online. All related code and installation scripts are
included in this artifact, allowing evaluators to reproduce results without additional downloads.


hardware unavailable in the QEMU emulation environment, and CVE-2024-0582, CVE-2024-47674, and
CVE-2024-53096 affect kernel versions other than
v6.6.0 used in this artifact.
(E2): Performance Evaluation (120 compute-minutes): This
experiment measures the overhead of DMG UARD and
ptcheck compared to baseline, reproducing Table 4

higher than those measured on actual Pixel 8 hardware
as reported in the paper. Nevertheless, the overhead
remains acceptable and similar trends are maintained.
Additionally, due to the instability of the QEMU
environment, we use median instead of average, unlike
in the paper.

```


## usenixsec2026-final109 — Bridging Bitcoin to Second Layers via BitVM2
- artifact: https://doi.org/10.5281/zenodo.17949747
- ref: doi 10.5281/zenodo.17949747
- paper: 

```
Description & Requirements

The artifact is permanently archived on Zenodo with DOI
10.5281/zenodo.17949747, ensuring long-term availability as
required for the Artifacts Available badge.
A.2.3

Hardware dependencies

Minimum requirements:
• CPU: x86_64 or ARM64 (Apple Silicon supported)
• RAM: 16GB minimum, 24GB recommended
• Disk: 10GB free space

Software dependencies

Required: Rust 1.70+ (per rust-toolchain.toml), Cargo,
Git, Bitcoin Core 25.0+, Risc0 toolchain.
Optional: Docker (containerized regtest), CUDA toolkit
(NVIDIA GPUs).

All dependencies are available via standard package managers. Detailed installation in Section 1.3.1.
A.2.5

Benchmarks

This section describes the environment required to evaluate

Network activity: Requires internet connectivity to download dependencies (Rust crates, Risc0 toolchain). Bitcoin
Core will bind to network ports for the regtest node.

Step 1: Clone repository
git clone https://github.com/bitvm/bitvm
cd bitvm

```


## usenixsec2026-final124 — Libra: Pattern-Scheduling Co-Optimization for Cross-Scheme FHE Code Ge
- artifact: https://zenodo.org/records/17962002
- ref:  
- paper: 

```
efficient code generation by co-optimizing cross-scheme computational patterns with hardware-aware scheduling strategies.
This artifact includes: (i) the Libra compiler source code, (ii)
the underlying FHE libraries (based on FlyHE), (iii) comprehensive benchmarks (microbenchmarks and end-to-end applications), and (iv) scripts that automate compilation, execution,
result collection, and figure/table generation to reproduce the
paper’s key results.


Description & Requirements

A.2.1

Security, privacy, and ethical concerns


It performs standard compilation and benchmarking on the
included workloads and does not require disabling security
mechanisms or handling sensitive data. All evaluations use
only synthetic or publicly available benchmark datasets. The
workflow is self-contained and does not permanently modify
the host system configuration. The only external interaction

Hardware dependencies

To reproduce the performance results reported in the paper, we
recommend the same GPU platform used in the evaluation:
• GPU: NVIDIA A100 GPGPU (≥ 40 GB).
• CPU Architecture: AMD64.

Software dependencies

The artifact has been tested on Ubuntu 22.04. We provide a
Docker image to ensure environment consistency.
Docker (Pre-installed): The image includes all toolchains
and heavily-compiled dependencies (e.g., Polygeist, LLVM,

Manual Build Requirements:
• CMake ≥ 3.31.1; Ninja ≥ 1.10.1
• GCC/G++ ≥ 13.1.0; Clang/Clang++ ≥ 22.0.0
• CUDA Toolkit ≥ 12.4
• LLVM & MLIR ≥ 22.0
• NTL ≥ 11.5.1; GMP ≥ 6.2.1

Benchmarks

All benchmarks used in the paper are included under
Libra_full_bench, consisting of:
• Microbenchmarks: Individual FHE operators.
• Applications: End-to-end workloads.

3. The source code, data, and required dependencies for the
artifact are available in Security_Artifact/Libra.
Option B: Build from Source If not using Docker, install
all dependencies listed above and build the toolchain components from the repository root (Security_Artifact/Libra)
in the following order.
1. Build Polygeist:

(C1) Microbenchmark performance: Libra generates FHE
kernels that outperform or match the provided reproducible
baselines on microbenchmarks. This corresponds to results
shown in Figure 8.
```


## usenixsec2026-final173 — Semantics Over Syntax: Uncovering Pre-Authentication 5G Baseband Vulne
- artifact: https://zenodo.org/doi/10.5281/zenodo.17984911
- ref: doi 10.5281/zenodo.17984911
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


with all required dependencies pre-installed.
• A2. Constraint-driven toolchain. This component provides the full analysis and test generation pipeline, including specification preprocessing scripts, field dependency extraction, DSL-based mutation logic, and ASN.1
decoding/encoding utilities.
• A3. Test cases and proof-of-concept exploits. This



validate the A1 simulation testbed and A3 test cases. All required system libraries and runtime dependencies for these
components are pre-installed in the provided Docker image,
and reviewers are not required to compile or install additional
third-party software when using this option. Alternatively,
reviewers may access a pre-configured remote desktop environment that hosts the same Docker-based setup.
The A2 constraint-driven toolchain runs natively on

Ubuntu 22.04 using Python 3.10.12. All Python dependencies are open-source and can be installed via
pip3. For transparency and reproducibility, we provide an
installed_packages.txt file generated via pip3 freeze,
which enumerates the exact Python package versions used in
our experiments.
The artifact does not rely on any proprietary or licensed software, vendor-specific SDKs, firmware images, or restricted

Hardware dependencies

None. The artifact does not require any specialized 5G wireless hardware. All evaluations can be completed entirely in
a simulation environment. In particular, the artifact does not
require SDR devices (e.g., USRP), commercial smartphones,
SIM cards, antennas, or any over-the-air radio infrastructure.

or AMD CPUs) and does not require GPU acceleration. A machine with 32 GB of RAM and 80 GB of available disk space
is recommended. The full T3 inter-IE pipeline requires more
RAM due to peak memory usage during multi-process serialization; evaluators with less RAM may use the lightweight
verification alternatively. The artifact has been verified on the
following configuration:
• CPU: 12th Gen Intel Core i7-1260P (12 cores)

Software dependencies

Benchmarks

This work does not rely on traditional machine-learning
benchmarks or pre-collected datasets. Instead, the experiments are driven by protocol specifications, reference protocol

serves as the target system under test rather than a benchmark dataset.
All inputs required for the experiments are either publicly
available (3GPP specifications) or included in the artifact and
do not require any external datasets.

A.3

22.04 LTS (x86-64). No proprietary software is required.
E1 — Python environment (A2). The constraint-driven
toolchain (A2) requires Python 3.10 on Ubuntu 22.04. Evaluators may start from a clean Docker container as the host
environment:
```


## usenixsec2026-final10 — Trust Nothing: RTOS Security without Run-Time Software TCB
- artifact: https://doi.org/10.5281/zenodo.20259753
- ref: doi 10.5281/zenodo.20259753
- paper: 

```
without Run-Time Software TCB
Eric Ackermann, Sven Bugiel
CISPA Helmholtz Center for Information Security

A
A.1

vulnerabilities in application software, operating system kernels, and peripherals threaten the embedded device integrity.
Existing computer-architectural defenses fully consider at
most two of these threat vectors in their security model.
Our paper aims at addressing this gap using a novel capability architecture. To this end, we combine a token capability
approach suitable for building an untrusted operating system
with protection against malicious devices without requiring

hardware changes to peripherals.
First, we develop and evaluate Bredi, a full FPGA implementation of our capability architecture around legacy hardware components. Further, we present a soft real-time operating system Skadi based on Zephyr that has no run-time
software TCB. To this end, we disaggregate Zephyr’s subsystems into small, mutually isolated components. All subsystems that exist at run time, including scheduler, allocator
and DMA drivers, and all peripherals are fully untrusted. We
believe that our work offers a foundation for more rigorous
security-by-design in tomorrow’s security-critical embedded

benchmark executions.

A.2

Description & Requirements


Requirements for building the FPGA SoC. Bredi targets
the Digilent Genesys2 FPGA board. Building the SoC for this
board requires Xilinx Vivado version 2024.2 with a license
appropriate for the xc7k325tffg900-2 part (evaluation license
should be sufficient). Furthermore, we utilize Xilinx’ proprietary AXI ethernet subsystem. To this end, building the SoC
requires the appropriate licenses (EF-DI-TEMAC-PROJ or

Requirements for building Skadi RTOS. We provide
scripts for building Skadi from source. This requires a workstation with Ubuntu 22.04, root access and sufficient free disk
space (>32 GB).
Requirements for running the Artifact. All of our evaluations were conducted on a Digilent Genesys2 FPGA board.
Furthermore, we require an SD card, (optionally, for the Arty
A7) a suitable USB JTAG debugger (we use a Digilent HS2),

Included benchmarks.
The artifact comprises the following benchmarks relevant
for our performance claims:
• FPGA chip area can be reported by Vivado in GUI mode
(table 2 in the paper).
• ASIC chip area can be reported using our provided

microbenchmark
sim_capability_test (table 6, 7 in the paper).
• We use an existing microbenchmark from Zephyr
syscall_perf (table 7 in the paper).



• We ship the coremark and the stream benchmarks in
a ported version for measuring compute performance
(table 8 in the paper).
• For network benchmarks, we use the ping and iperf utilities with a ported zperf sample, a custom shell script
```


## usenixsec2026-final18 — SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity
- artifact: https://doi.org/10.5281/zenodo.20209122
- ref: doi 10.5281/zenodo.20209122
- paper: 

```
Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

No special hardware is required, however a CUDAcompatible GPU is recommended for the AutoRobust case
study. The full reproduction of 20 seeds is computationallyintensive, therefore, we recommend running a single seed
(reproducibility/reproduce-one-seed.sh).
A.2.4

Software dependencies

• python3.9 & python3.10 are both required as the case
studies have varying dependency requirements
• Docker Engine & Docker Compose are required for
the Link and S QIRL case studies.

• The python dependencies for each of the case
studies can be found in reproducibility/envs/
{case-study-name}.txt, with the venv setup automated by reproducibility/setup-envs.sh.

A.2.5


Benchmarks

• AutoRobust:
the
dataset
needs

• S QIRL: no external data required, SQLi MicroBenchmark (S MB) docker file is provided.
• MiniCAGE: the MiniCAGE ACD environment is provided. The rl-reliability-metrics package is
cloned and installed automatically by setup-envs.sh.

A.3


```


## usenixsec2026-final55 — Fuzzing Open-Source GPU Hardware with SIMT Program Generation
- artifact: https://doi.org/10.5281/zenodo.20321391
- ref: doi 10.5281/zenodo.20321391
- paper: 

```
Hardware with SIMT Program Generation
Zibo Gao†§ , Jie Wang†§ , Qihang Zhou†§ , Lixiao Shan†§ , Junjie Hu†§ , Xiaoqi Jia †§ , and Zhiqiang Lv†§
† Institute of Information Engineering, Chinese Academy of Sciences.
§ School of Cyber Security, University of Chinese Academy of Sciences.
{gaozibo,wangjie2024,zhouqihang,shanlixiao,hujunjie,jiaxiaoqi,lvzhiqiang}@iie.ac.cn


available GPU hardware fuzzer exists for comparison. We
therefore adapted Cascade and DiveFuzz to GPUs as baselines that generate instruction-level data and control flows.
Experimental results show that FuzzGPU achieves higher
coverage and throughput than the GPU ports of Cascade and
DiveFuzz. We also package the Devices Under Test (DUTs),
including Vortex and Ventus OpenGPGPU. Overall, this artifact demonstrates FuzzGPU’s functionality as presented in

Description & Requirements

A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

To reproduce the performance results, we recommend using
an Intel(R) Xeon(R) 6982P-C system with 192 vCPUs and
768 GB of RAM.
A.2.4

Software dependencies

Our artifact requires a Linux distribution, make, and Docker
v29.5.3 as prerequisites. The Dockerfile automatically installs the remaining dependencies. Experiments are designed
to run inside the Docker container.
A.2.5

Benchmarks

FuzzGPU was evaluated on two open-source GPUs, Vortex
and Ventus OpenGPGPU. We also compare its performance
against GPU ports of two CPU fuzzers: Ported-Cascade and
Ported-DiveFuzz.

and installs all dependencies and configures the metadata.
A stable Internet connection is required to avoid missingfile errors. Proxy options are provided in the Makefile and
Dockerfile. This step may take up to 24 machine-hours and
consume ~200 GB of disk space.

How to access

```


## usenixsec2026-final57 — Do Not Mention This to the User: Detecting and Understanding Malicious
- artifact: https://doi.org/10.5281/zenodo.20285751
- ref: doi 10.5281/zenodo.20285751
- paper: 

```
Description & Requirements

The artifact has two top-level components: data/ holds the
released benchmark CSVs, and code/ holds the reproducibility framework and the deterministic analysis suite. Because
the agent-skill ecosystem is live and final malicious labels require manual behavioral verification, the framework defaults
to a small-batch experiment; environment variables control

Hardware dependencies

A modern x86-64 Linux machine with ≥ 4 CPU cores, 8 GB
RAM, and 20 GB free disk suffices for the default small-batch
experiment; Docker is required for dynamic execution. No
GPU is needed—the default Nova-tracer recording mode and

Software dependencies

The host requires Python 3.10+, Docker, Git, curl, GNU
timeout (macOS: expose coreutils gtimeout as timeout),
and a local Claude Code CLI login or an Anthropiccompatible API key (both documented in the README); the
optional CC triage additionally needs jq. Host-side Python

dependencies are in code/requirements.txt. The default
reproduction pulls the prebuilt sandbox image (≈ 300 MB), so
the host needs no strace, tcpdump, or Nova-tracer hooks—
they ship inside the image. A SkillsMP API key is required
for the default crawl (free at skillsmp.com); a GitHub token
is optional but recommended for larger downloads.

Benchmarks

The released benchmark, from the paper’s January 2026 measurement of two registries (skills.rest, skillsmp.com), consists
of:
• data/skills_dataset.csv:
the Tier-1 snapshot of 98,380 skills across 11,246 repositories,

requirements.txt, then launch python3 helper.py.
For first-time setup, step through 1. init (writes
code/.env), 2. doctor (host checks), and 3. image
(pulls the prebuilt image; load-tar for the offline tarball, full-cpu/full-custom for local builds). Menu
actions 4. run, 5. status, 6. clean run the small-batch
experiment, inspect/edit configuration, and prune outputs.

(C1): The released benchmark CSVs load with the documented schema, and the curated Tier-3 dataset contains

exactly 157 behaviorally-confirmed malicious skills (21
from skills.rest, 136 from skillsmp.com), matching Table
2 of the paper. This is validated by experiment E1.
(C2): The artifact can run the framework’s end-to-end analysis workflow on a bounded sample: crawl, mapping,

requirements.txt, then run taxonomy_counts.py,
rq1_landscape.py,
cooccurrence.py,
and
hypothesis_tests.py (code/scripts/ 09–11
wrap the last three). All four read only the released data/malicious_skills.csv; analysis/

```


## usenixsec2026-final90 — Low-Cost Hard-Label Adversarial Attack with Theoretical Foundations
- artifact: https://doi.org/10.5281/zenodo.20322560
- ref: doi 10.5281/zenodo.20322560
- paper: 

```
Description & Requirements

The full artifact provides: (1) source code for the proposed
DPAttack method, including fixed-block-size, dynamic-blocksize, ℓ2 , Blacklight-aware, and randomized-defense variants;
(2) scripts and wrappers for reproducing the main experiments and baselines; (3) analysis utilities for BFS, frequency
statistics, gradient-alignment, cosine-similarity evolution, and

preparation, expected directory structure, hardware/runtime
requirements, Quick Start usage, and commands for reproducing the paper’s main tables and figures.
A.2.1

Security, privacy, and ethical concerns


Hardware dependencies

Our experiments were primarily conducted on a single
NVIDIA RTX A6000 GPU with 48GB VRAM. This is the
hardware used in our experiments, not a strict minimum requirement.
Table 1: Observed hardware usage for representative settings.

several days, depending on hardware, query budgets, dataset


availability, API rate limits, and whether all baselines are rerun. We therefore recommend starting from the Quick Start
and then reproducing representative experiments.
A.2.4

Software dependencies

We use Ubuntu with Conda for environment management,
and recommend Python 3.11. Unless otherwise specified in
the corresponding sections, the test experiments described
below can be executed directly in the environment provided

Dockerfile.quickstart, requirements_quickstart.
txt, and requirements_quickstart_docker.txt. Depending on the local Docker configuration, Docker commands
may require sudo. Some experiments further require external
public datasets, pretrained checkpoints, third-party repositories, or commercial API credentials; these requirements are
documented in the repository README or explicitly noted
in the corresponding experiment sections.

Benchmarks

The artifact evaluation supports experiments on CIFAR-10,
ImageNet-1K and ObjectNet/CLIP. We provide small subsets of the public datasets for efficient evaluation, while the
full large-scale public datasets and some third-party repositories are not redistributed directly. The following sections and
README explain how to obtain these resources and place

quickstart.md to install the required dependencies with
pip.
Full artifact. The following steps 2-3 are optional for artifact evaluation. The Conda environment built in the Quick
Start above can be reused for the following evaluation experiments, requiring only a small number of additional package
installations when necessary.


that the software environment, checkpoint loading, and attack
pipeline are functioning correctly.
Docker command:
docker run --rm --gpus all dpattack-cifar10- \
```


## usenixsec2026-final102 — Retrofit: Continual Learning with Controlled Forgetting for Binary Sec
- artifact: https://doi.org/10.5281/zenodo.20339141
- ref: doi 10.5281/zenodo.20339141
- paper: 

```
Description & Requirements

The artifact contains two independent implementation directories: Malware_Detection/ and Binary_Analysis/, which
should be run in their corresponding dependency environments.
⋆ Co-first authors. B Corresponding author: heyilinge0@gmail.com


The README describes the repository layout, dependencies,
data preparation, and experiment commands. Due to licensing and redistribution constraints, we provide instructions for
obtaining the Transcendent dataset, the CAPYBARA dataset,
and the CodeT5-base model through their official channels.
To further facilitate reproducibility, we also provide the processed Transcendent features and the models used in our main
results.

Hardware dependencies

The paper-level results were obtained on NVIDIA RTX
A6000 GPU servers. Malware_Detection/ can also run on
CPU. Binary_Analysis/ is more computationally demanding, so CUDA-capable NVIDIA GPUs are recommended for
the full workflow.

Software dependencies

The two components should be installed in separate environments using Malware_Detection/requirements.txt
and Binary_Analysis/requirements.txt. The binaryanalysis workflow uses the BinT5 Docker environment with
Python 3.10.
The requirements files specify the Python-package dependencies required for evaluation and visualization; the binaryanalysis workflow additionally relies on the BinT5/CodeT5

Benchmarks

The benchmarks cover malware detection under temporal
drift and binary summarization across decompilation levels.
For malware detection, we use the Transcendent dataset and
MLP classifiers. For binary summarization, we follow the

benchmark data, require released checkpoints, or require GPU
execution. A successful run exits with status code 0 without
Python tracebacks or error messages.
For Binary_Analysis/, run the following check inside
the BinT5 environment:
python - <<'PY'

Malware_Detection/requirements.txt

A.4

This section covers the R ETROFIT results in Figure 5 and
Figure 6.

Preparation: Install dependencies following the
README. For the complete R ETROFIT workflow, prepare the processed Transcendent feature files and yearly
train/test splits. For the Figure 5 evaluation-and-plotting
workflow, download the released checkpoints and the
required dimension-reduced test inputs.
Execution: To run the complete R ETROFIT workflow,

values may differ slightly from the paper because of hardware
differences, random seeds, and non-determinism; the expected
result is to reproduce the same overall trends.

```


## usenixsec2026-final111 — PICASSO: Scaling CHERI Use-After-Free Protection to Millions of Alloca
- artifact: https://doi.org/10.5281/zenodo.20353117
- ref: doi 10.5281/zenodo.20353117
- paper: 

```
enables provenance tracking of capabilities to their respective allocations via a hardware-managed provenance-validity
table, allowing bulk retraction of dangling pointers without
needing to quarantine freed memory. Colored capabilities
significantly reduce the frequency of capability revocation
sweeps while improving security. Colored capabilities are
realized in PICASSO, an extension of the CHERI-RISC-V

PICASSO is demonstrated using the SPEC CPU benchmark
and real-world SQLite, PostgreSQL, and gRPC benchmarks.

A.1

Abstract

• A bare-metal hardware simulation environment based on
the Bluespec simulator. This environment can be used
to reproduce performance evaluation using the MiBench
suite and Coremark.
• An FPGA-based evaluation environment with support for
colored-capability-enabled CheriBSD. This environment

benchmarks (SPEC, SQLite, PostgreSQL, and gRPC).
Note: The Artifact Evaluation Committee evaluated
the artifact in the QEMU emulation and bare-metal
hardware simulation environments. Further details on
the reproduced experiments are provided in § A.4.2.


Description & Requirements

A.2.1

Security, privacy, and ethical concerns


software-based approaches for vulnerability detection, such as
sanitizer-instrumented binaries. Consequently, the PICASSO
artifact does not provide additional capabilities beyond such
existing tools. We therefore do not expect security, privacy,
or ethical concerns associated with the PICASSO artifact.


Hardware dependencies

The QEMU-based emulation environment, the bare-metal
hardware simulation environment, and the build environment
for software artifacts targeting each evaluation environment
require a x86_64 Linux machine with Docker installed. The

and a host machine with JTAG/Vivado Hardware Manager.
A.2.4

Software dependencies

The artifact provides a Dockerfile for the QEMU-based emulation environment, the bare-metal hardware simulation

environment, and the build environment for software artifacts. The Dockerfile has been tested on Ubuntu Server
24.04.4 LTS using Docker version 29.1.3 obtained from
https://ubuntu.com/server
Xilinx/AMD Vivado Design Suite 2019.1 and license
```


## usenixsec2026-final157 — FLOSS: Fast Linear Online Secret-Shared Shuffling
- artifact: https://doi.org/10.5281/zenodo.20278557
- ref: doi 10.5281/zenodo.20278557
- paper: 

```
Description & Requirements

FLOSS enables efficient online shuffling in the two-party
computation (2PC setting). We provide shuffling benchmarks for FLOSS, the constant round malicious secure permutation network by Mohassel et al. (PermNet), Oblivious Punctured Matrix from Song et al. (OPM), and the
canonical log (n)-round malicious-secure permutation network circuit from Waksman (SimplePermNet). We also
provide a case-study applying our shuffling protocol to

several sorting benchmarks. These sorting benchmarks include MP-SPDZ’s sorting network (SortNet), MP-SPDZ
quicksort combined with shuffling protocols (StS[FLOSS],
StS[OPM], StS[PermNet], StS[SimplePermNet]), and radixsort combined with shuffling protocols (Radix[FLOSS],
Radix[PermNet], Radix[SimplePermNet]). We evaluate both
the preprocessing time (MP-SPDZ preprocessing generation,
any input-independent circuit computation) and the online

AWS credits. The minimal hardware requirements to run our
full set of our benchmarks is two AWS c5.18xlarge instances

(72 vCPUs and 144GB memory each), each running Ubuntu
22.04 LTS. We provide one-run scripts that automatically
instantiates the AWS instances with required dependencies

and benchmarks.
For reviewers without AWS access, we also support running
the full benchmark suite, including the pareto plots, on local
hardware comparable to the AWS setup: either two local
Ubuntu servers (each with ≈72 hardware threads and 144GB
memory, connected over a high-bandwidth network), or a

single large local Ubuntu server (with ≈144 hardware threads
and 288GB memory) partitioned into two Docker containers
that emulate the two parties. We provide a Dockerfile and
container scripts that automate installation and benchmarking
for this setup.
Ubuntu 22.04 LTS (recommended) or Mac OS X Sequoia is

required in order to run benchmarks on a single smaller local
computer, which only runs a subsample of our benchmarks
due to decreased compute power. We require that the user has
at least the compute power of at least 16 GB of memory and
an Apple M4 chip for CPU (or equivalent).
A.2.1

server hardware. The essential setup and reproduction steps
for all options are included directly below.
A.2.3

Hardware dependencies


FLOSS does not require any specialized hardware. Our experiments were performed on AWS c5.18xlarge instances, each
with 72 vCPUs and 144 GB memory. Reviewers without AWS
access can reproduce the full benchmark suite on comparable local hardware instead: either two local Ubuntu servers,
each with approximately 72 vCPUs and 144GB memory, or
a single large local Ubuntu server with at least 144 vCPUs
and 288GB memory, which we partition into two Docker containers of 72 vCPUs and 144GB memory each to emulate the

two parties. Different hardware configurations will affect the
concrete performance of FLOSS, but will result in a similar
performance gain over the baselines.
A.2.4
```


## usenixsec2026-final218 — BLE Theft Auto: Evaluating the Security of Aftermarket BLE-based Autom
- artifact: https://zenodo.org/records/20656773
- ref:  
- paper: 

```
Description & Requirements

The public artifact includes the notebooks ad_cluster.py
and scale_estimation.py, the wigledl.py WiGLE collection script, the proof.lean formal proof, the prebuilt cluetooth.apk Android app, and the scrubbed
karr-attack/karr/ Python implementation with secret
keys removed. The restricted artifact contains sensitive data

Software dependencies

None beyond the items listed in the Set-up section below. We
recommend a Linux environment for running the artifacts.
A.3.5


Hardware dependencies

A 64-bit machine is required; 8+ GB of RAM is recommended
for running the notebooks smoothly. The BLE scanner app
requires an Android device running Android 7.0 (API 24) or
newer.

Benchmarks

uv run marimo edit ad_cluster.py
uv run marimo edit scale_estimation.py
Android app: Install the pre-built cluetooth.apk on
your device. See the privacy notice in the Security, privacy,

and all dependencies, including the marimo notebook framework. No manual virtual environment setup is needed.
Alternatively, the public artifact includes a Dockerfile
and docker-compose.yml. After copying the restricted

A.5


effects, and avoid context dependencies to maximize reusability on new datasets. In scale_estimation.py, the estimator
function takes a sequence of serial numbers (integers) and
returns an estimated count; any incrementing identifiers representable as integers can be adapted to this estimator, not
just MAC addresses. In ad_cluster.py, the pipeline accepts
raw advertisement packets encoded as hex strings (one per
line) and runs the clustering algorithm. The hierarchical clustering function is pure and composable: future researchers

```


## usenixsec2026-final219 — SONIC: Concurrent Oblivious RAM & Data Structures for Low-Latency and 
- artifact: https://zenodo.org/records/20646913
- ref:  
- paper: 

```
Description & Requirements

• sonic/: SONIC, GraphMap, O2TH, PMCHAIN.
• baselines/sgx-baseline-container/: SGX baseline image.
• baselines/enigmap/: EnigMap baseline.
• baselines/graphos/: GraphOS baseline.

or evaluator data. It runs benchmark programs in ephemeral
Docker containers with SGX device passthrough. It does not
modify host data.
A.2.2

How to access

Hardware dependencies

• x86_64 Linux host with Intel SGXv2
• Azure Standard_DC32s_v3 instance, with 32 vCPUs,
256 GiB RAM, 192 GiB EPC
• /dev/sgx_enclave and /dev/sgx_provision (SGX

Software dependencies

Docker on x86_64 Ubuntu 22.04. The artifact includes Dockerfiles for the build toolchain.
Host sanity checks:

Benchmarks

(C6): O2TH and PMCHAIN benchmarks support the Figure 11 subORAM evaluation story. See E6.
A.4.2

Experiments

For a standard and representative SGX hardware environment,

full benchmark matrix in the paper takes ≈ 4 VM-days to run
for all single-server experiments. The multi-server experiment
additionally requires significant effort for provisioning on
multiple machines and high (≈ $800) costs.
Therefore, for artifact evaluation, we recommend running
representative anchors to corroborate all claims: exact plotted parameter configurations with bounded access counts.

(E6): Single-node subORAM benchmarks. [15m human; 1h
compute.]
# Host shell:
cd "$HOST_ARTIFACT_ROOT"
python3 experiment.py suboram --anchor
python3 experiment.py suboram --full --commands

```


## woot2026-paper1 — LIMA: Defining, Benchmarking and Detecting Cross-Layer Vulnerabilities
- artifact: https://doi.org/10.5281/zenodo.20075284
- ref: doi 10.5281/zenodo.20075284
- paper: https://www.usenix.org/conference/woot26/presentation/sen

```
Artifact for LIMA: Defining, Benchmarking and Detecting Cross-Layer
Vulnerabilities in LLM Inference Frameworks
Sanjib Kumar Sen
ssen@islander.tamucc.edu
Texas A&M University-Corpus Christi


Ollama, and LocalAI enable users to run large language models (LLMs) on local hardware without relying on remote
services. However, these frameworks often load communityshared model files that may contain malicious payloads. We
define the Local Inference framework–Model Attack surface
(LIMA) as the set of vulnerabilities triggered when LIFs process untrusted model artifacts.
To understand the impact of LIMA, we collected 60 publicly disclosed vulnerabilities across four popular open-source
LIFs and curated them into a reproducible dataset. Our analysis derives a six-class taxonomy of root causes, showing that

– README: the detailed instructions (i.e., commands, requirements, expected output) on how to reproduce the 58
vulnerabilities with different configurations (e.g., timeout);
– run_all_pocs.sh: the script to run the 58 vulnerabilities included in LIMABench.
• LIMAScan – Our taxonomy-driven dynamic testing tool,
which includes:
– README: the detailed instructions on how to reproduce

Requirements and Setup

To successfully reproduce the results from LIMABench and
LIMAScan, the following hardware and software requirements are recommended:
• CPU: Minimum 4 cores (8+ recommended for parallel
container startup). An x86_64 host is required for several

• Software: Docker ≥ 20.10 with Docker Compose, Python
≥ 3.9, curl, and standard Unix utilities (e.g., bash,
grep, awk). The vLLM container additionally requires the
NVIDIA Container Toolkit2 for GPU passthrough.
• Operating System: Ubuntu 22.04 LTS or other modern
Linux distributions are recommended. macOS is partially

minutes, depending on whether required dependencies and
container images are already available locally.

where the result label is one of following four options:
• CRASHED: Server died (e.g., OOMKilled, non-zero exit, or
health check failed);

```


## woot2026-paper12 — SEMSAN: a Configurable Sanitizer for Detecting System-Level Semantic B
- artifact: https://doi.org/10.5281/zenodo.20020039
- ref: doi 10.5281/zenodo.20020039
- paper: https://www.usenix.org/conference/woot26/presentation/sanft

```
implementations, test suites, and benchmark scripts used to
reproduce the evaluation results.

A.1

Description & Requirements

benchmarks (Section 7.2). This is supported by experiment (E2).
(C3): S EM S AN’s performance overhead ranges from 3.15%
(System Call Sanitizer) to 20.85% (Directory Ownership
Sanitizer) in the micro-benchmarks, and introduces negligible overhead (< 5%) on real-world workloads (PostgreSQL pgbench, Apache HTTP server) in the macrobenchmarks (Section 7.3). This is supported by experiment (E3).

Hardware dependencies

specialized hardware is needed.
A.1.4

A.2.1

c u r l −− p r o t o ’= h t t p s ’ −− t l s v 1 . 2 − s S f −L \

benchmark automation scripts. In addition, we make the
artifact available on Zenodo https://doi.org/10.5281/
zenodo.20020039.
A.1.3

Set-up

Software dependencies

The artifact relies on the Nix package manager to provide a
fully reproducible build environment. All other dependencies
1


micro- and macro-benchmarks.
How to: Run the micro-benchmark (approx. 20 minutes):
n i x r u n . # a r t i f a c t − e v a l . micro − benchmark
Then run the macro-benchmark (approx. 1 hour):
n i x r u n . # a r t i f a c t − e v a l . macro − benchmark
Results for Claim 3: The micro-benchmark produces

3.15% and 20.85%. The macro-benchmark produces
results comparable to those shown in the Apache and
PostgreSQL figures in Section 7.3, with overhead below
5%.
2


```
