start: ## start the server
	python src/main.py

build-protocol: ## build protobuf protocol
	python -m grpc_tools.protoc -I./protos --python_out=./src --pyi_out=./src --grpc_python_out=./src ./protos/helloworld.proto