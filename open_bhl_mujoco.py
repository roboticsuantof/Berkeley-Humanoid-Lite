import time
from pathlib import Path

import mujoco
import mujoco.viewer


PROJECT_ROOT = Path(__file__).resolve().parent

xml = Path(
  PROJECT_ROOT
/"source"
/"berkeley_humanoid_lite_assets"
/"data"
/"robots"
/"berkeley_humanoid"
/"berkeley_humanoid_lite"
/"mjcf"
/"bhl_scene.xml"
).resolve()

print(f"Abriendo modelo: {xml}")

model = mujoco.MjModel.from_xml_path(str(xml))
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)
