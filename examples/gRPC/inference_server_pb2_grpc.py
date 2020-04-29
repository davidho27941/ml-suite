# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import inference_server_pb2 as inference__server__pb2


class InferenceStub(object):
    """Inference server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Inference = channel.stream_stream(
                '/inference_server.Inference/Inference',
                request_serializer=inference__server__pb2.ListOfArrays.SerializeToString,
                response_deserializer=inference__server__pb2.ListOfArrays.FromString,
                )


class InferenceServicer(object):
    """Inference server
    """

    def Inference(self, request_iterator, context):
        """Inference
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InferenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Inference': grpc.stream_stream_rpc_method_handler(
                    servicer.Inference,
                    request_deserializer=inference__server__pb2.ListOfArrays.FromString,
                    response_serializer=inference__server__pb2.ListOfArrays.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inference_server.Inference', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inference(object):
    """Inference server
    """

    @staticmethod
    def Inference(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/inference_server.Inference/Inference',
            inference__server__pb2.ListOfArrays.SerializeToString,
            inference__server__pb2.ListOfArrays.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)