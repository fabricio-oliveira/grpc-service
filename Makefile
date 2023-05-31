start: ## start the server
	python src/main.py

build-protocol: ## build protobuf protocol
	@echo "import sys\nfrom pathlib import Path\nsys.path.append(str(Path(__file__).parent))" > ./src/generated/__init__.py
	@PYTHONPATH=./src python -m grpc_tools.protoc \
		--python_out=./src/generated \
		--pyi_out=./src/generated \
		--grpc_python_out=./src/generated \
		--proto_path protos/ \
		comicbook/company.proto

clean: ## clean cache files
	@find . | grep -E '(/__pycache__$$|\.pyc$$|\.pyo$$)' | xargs rm -rf