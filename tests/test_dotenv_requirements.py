import os
from dotenv import load_dotenv

def test_dotenv():
  load_dotenv()
  all_envs_keys = os.environ.keys()
  all_dotenv_env = []
  with open("DOTENV", "r") as dotenv:
    for env in dotenv:
      all_dotenv_env.append(env)

  print("dotenv", all_dotenv_env)
  print("envs in device", all_envs_keys)
  assert all(env in all_envs_keys for env in all_dotenv_env)