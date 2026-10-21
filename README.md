# AutoDriveStack

Open-source autonomous driving full-stack framework for perception, planning, simulation, and deployment.

AutoDriveStack is a modular autonomous driving framework focused on enabling developers and researchers to build practical driving pipelines from data to simulation.

This repository is designed to provide:
- a clean modular architecture
- quick demo generation
- path planning examples
- visualization support
- extensible engineering structure

## Project goals

- Build a usable autonomous driving framework foundation
- Support trajectory planning and lane-following demos
- Provide a scalable structure for future perception and simulation modules
- Keep setup simple for local development and Docker-based runs

## Project structure

```bash
AutoDriveStack/
├── README.md
├── LICENSE
├── .gitignore
├── Makefile
├── requirements.txt
├── docker/
├── config/
├── packages/
├── scripts/
├── examples/
├── data/
```

## Quick start

### 1. Clone
```bash
git clone https://github.com/yifengzhong-cat/AutoDriveStack.git
cd AutoDriveStack
```

### 2. Create environment
```bash
make setup
```

### 3. Run demo
```bash
make demo
```

## Demo

This project currently includes a basic lane-following trajectory demo.

The demo generates a sample path and plots the vehicle motion in a 2D environment.

## Roadmap

- Phase 1: project foundation and environment setup
- Phase 2: planning and lane following demo
- Phase 3: perception module
- Phase 4: simulation and telemetry dashboard
- Phase 5: deployment and community improvements

## License

MIT License
