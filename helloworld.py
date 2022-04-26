from metaflow import FlowSpec, step, kubernetes


class HelloArgoFlow(FlowSpec):

    @step
    def start(self):
        print("HelloFlow is starting.")
        self.next(self.hello)

    @kubernetes(image='python',
                secrets=['s3-secret'])
    @step
    def hello(self):
        print("HelloFlow says HELLO.")
        self.next(self.end)

    @step
    def end(self):
        print("HelloFlow is all done.")


if __name__ == '__main__':
    HelloArgoFlow()