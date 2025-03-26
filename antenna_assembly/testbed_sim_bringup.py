import omni
from omni.isaac.kit import SimulationApp
import time
import numpy as np
import math

# Initialize Isaac Sim application
simulation_app = SimulationApp()

from pxr import Usd, UsdGeom, Gf

# Function to load USD file into the scene
def load_usd_object(usd_path, position, rotation):
    stage = Usd.Stage.Open(usd_path)  # Load the USD stage
    if not stage:
        print(f"Failed to load USD file at {usd_path}")
        return None

    # Extract root of the stage
    root_prim = stage.GetPseudoRoot()

    # Create a new prim in the current scene and reference the USD file
    new_prim = omni.usd.get_context().get_stage().DefinePrim("/World/" + root_prim.GetName(), root_prim.GetTypeName())

    # Set position (translation) and rotation (quaternion)
    transform = UsdGeom.Xformable(new_prim)
    xform_op = transform.AddXformOp(UsdGeom.XformOp.TypeTranslate)
    xform_op.Set(Gf.Vec3f(position[0], position[1], position[2]))

    # Rotate using a quaternion
    quat = Gf.Quatf(rotation[0], rotation[1], rotation[2], rotation[3])
    rotation_op = transform.AddXformOp(UsdGeom.XformOp.TypeRotateXYZ)
    rotation_op.Set(quat)

    return new_prim

# Function to set up objects at specific poses
def setup_objects():
    # Define the USD files and their corresponding poses (position + rotation)
    objects_info = [
        {
            "usd_path": "/home/rp/abhay_ws/ISAM-sim/assets/usd/al_8020.usd",  # Specify path to your USD file
            "position": [0, 0, 0],  # Position (x, y, z)
            "rotation": [1, 0, 0, 0]  # Rotation as quaternion (w, x, y, z)
        },
        {
            "usd_path": "/home/rp/abhay_ws/ISAM-sim/assets/usd/al_8020.usd",  # Specify path to your USD file
            "position": [1, 2, 0],  # Position (x, y, z)
            "rotation": [0, 1, 0, 0]  # Rotation as quaternion (w, x, y, z)
        }
    ]

    for obj_info in objects_info:
        usd_path = obj_info["usd_path"]
        position = obj_info["position"]
        rotation = obj_info["rotation"]
        load_usd_object(usd_path, position, rotation)

# Main function to set up environment
def main():
    setup_objects()
    # Allow time for objects to load
    time.sleep(2)

    # Run the simulation or further setup
    print("Objects placed in the scene. You can start the simulation.")

if __name__ == "__main__":
    main()
