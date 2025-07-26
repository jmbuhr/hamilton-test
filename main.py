
import module
from hamilton import driver
from hamilton.execution import executors

dr = (
    driver.Builder()
    .with_modules(module)
    .enable_dynamic_execution(allow_experimental_mode=True)
    .with_local_executor(executors.SynchronousLocalTaskExecutor())
    .with_remote_executor(executors.MultiProcessingExecutor(max_tasks=5))
    .build()
)


def main():
    r = dr.execute(["result"])
    print(r['result'])

if __name__ == "__main__":
    main()
