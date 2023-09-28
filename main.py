import os
from qiskit.test.reference_circuits import ReferenceCircuits
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from dotenv import load_dotenv
load_dotenv()

name=os.environ["IBM_NAME"]
 
 
service = QiskitRuntimeService(name=name)
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(ReferenceCircuits.bell())
print(f"job id: {job.job_id()}")
result = job.result()
print(result)

