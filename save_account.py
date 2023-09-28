import os
from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
load_dotenv()
 
token=os.environ["IBM_TOKEN"]
name=os.environ["IBM_NAME"]

QiskitRuntimeService.save_account(channel="ibm_quantum", token=token, name=name, overwrite=True)
