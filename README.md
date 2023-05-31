# grpc-example
This is grpc service which was created using Python with grpcio with the educational proposal.
Feel free to use it as the base of your study.

## stack
For this project was used Python (3.9.6), pip (21.2.4) with grpcio.
So, before run the project check that you have the correct version of python and pip.

## to run:
```sh
pip install -m requirements.txt
make start
```

## to use
to consume this grpc service is necessary a client of grpc. 
a really good one is the [grpc-client-cli](https://github.com/vadimi/grpc-client-cli)

So, if you installed the client mentioned above. To connect the server with this client it's necessary just to run the command below:  

```sh
grpc-client-cli localhost:50051
```
