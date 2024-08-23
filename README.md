# Synthetic Datasets for Semantic Segmenation of Water Bodies in Images

Synthetic dataset generator and accompalying large-scale dataset of photorealistic randomized water bodies, built for training binary semantic segmentation models and improving their performance in Out-of-Distribution scenarios.

The application performs a wide variety of randomizations to maximize the diversity of generated datasets. These include randomizatios of water attributes (e.g., colour, reflection intensity, foaming, depth), environment attributes (e.g., light intensity, skybox material, rain intensity, fog density), and post-process effects (e.g., ISO noise, Depth of Field, Black and White, Raindrops on lens).

A configuration file can be provided in order to control and customize many of these elements.

These applications were made using the [Unity Perception package](https://github.com/Unity-Technologies/com.unity.perception), which provides tools for generating randomized synthetic CV datasets with a wide variety of ground-truth annotations.

The Labels that the dataset provides are in the form of Binary Semantic Segmentation masks.


### Configuration File

Several aspects of the dataset generation can be controlled using a JSON config file that is provided to the application. A sample config file is provided [here](./scenarioConfiguration.json).

The configuration file includes two main sections: (a) **constants**, (b) **randomizers**.

In the **constants** block, you specify:
* `iterationCount`: The number of Iterations the simulation should run for. Each Iteration produces one annotated frame. E.g. to generate 1000 images in your dataset, you should set thus value to 1000.
* `framesPerIteration`: The number of frames to render per Iteration. For some of the effects to become fully visible as they progress over time (e.g., Raindrops on lens effect), the value is set to 20. The value must match the Perception Camera's `frames between captures` attribute.
* `randomSeed`: The seed used for randomization. This generator uses Perception's randomization framework, which generates deterministic random numbers based on a provided seed. This helps you replicate datasets by keeping your seed value and randomization settings unchanged.


In the **randomizers** block of the JSON config file, you control the behavior of Perception Randomizers included in the project. Each Randomizer has one JSON block in this file. `randomizerId` denotes the name of the Randomizer, and `items` are the list of settings that can be changed. To change the behavior for each `item`, what you will need to modify is the `value` nested inside. In addition, some Randomizers can be completely disabled. We will now go through all the available Randomizers and their settings:

* **`WaterStylized2FoamingRandomizer`**: Controls the foaming effect (foam size) appearing on the surface of the water
  * `foamSize`: Controls the foam size.
  * `enableFoam`: Controls whether a foam effect is enabled or not.
 
* **`WaterStylized2ColorRandomizer`**: Controls the colour of the water. If disabled a single colour will be used in all images.

* **`WaterLevelRandomizer`**: Controls the level of the water plane.
  * `waterLevelRise`: The amount to add/subtract from the transform Y position of the water gameObject. Values are sampled from a normal distribution with `mean=0.0` and `stddev=1.0`. Positive values result in the water moving upwards, and negative values moving downwards. Change the `min` and `max` values nested inside this block to modify the water level. Prefer to chose values between the range [-2, 2].

* **`WaterStylized2ReflectionRandomizer`**: Controls the intensity of the reflections of the surrounding area on the surface of the water.
    * `reflectionStrength`: Sets the intensity of the reflections. 
    * `distortion`: Control the amount to which the reflections are distorted in the water's surface.

* **`WaterStylized2DepthRandomizer`**: Controls the intensty of the reflections of the surrounding area on the surface of the water.
    * `verticalDepth`: Controls the vertical depth of the water. Lower values results in the ground beneath the water being visible from above.
    * `distanceDepth`: Controls the distance from the camera in which the ground beneath the water becomes visible from above.
   

* **`LightIntensityRandomizer`**: Controls the intensity of the Directional Light in the scene.
    * `lightIntensity`: The intensity of the light source.
   
* **`FogDensityRandomizer`**: Controls the amount of fog present in the scene.
    * `fogDensity`: The density of fog.
    * `fogEnable`: Controls whether fog is enabled or not.

* **`SkyBoxRandomizer`**: Randomizes the HDRI skybox. If disabled, a single skybox will be used in all images.

* **`SkyColorRandomizer`**: Controls appearance of clouds in the sky (clear sky/overcast).
    * `lightIntensity`: Sets the ambient light intensity regarding the appearance of clouds in the sky.

* **`PostEffectsRandomizer`**: Controls a number of post processing effects on the camera.
  * `enablePostEffect`: The probability of a post-processing effect being applied. If the value is True, one of the following effects is enabled:
    * `bloom`: Increases the intensity of very bright highlights while applying a that applies a fullscreen layer of smudges or dust to five the impression of Lens Dirt.
    * `depthOfField`: Simulates the focus properties of a camera lens, making objects farther from the camera appearing out of focus.
    * `b&w`: Makes the image back and white.
    * `IsoNoise`: Simulates ISO noise appearing in cameras when the ISO values are too large.
    * `Raindrops`: Simulates raindrops falling on the camera lens.

* **`RainIntensityRandomizer`**: Controls the intensity of rain that is simulated using a Particle System. Switches between different intensities that control the amount of emission particles in the scene.
    * `lowIntensity`: Range [100-1000]
    * `mediumIntensity`: Range [1000-10000]
    * `highIntensity`: Range [10000-100000]
    * `enableRain`: Controls whether the Rain particle system is activated or not.


## Revert segmentation masks
The masks are generated in reverted format: Background is white and water pixels are black. You need to run the `black_and_white_reverse_all.py` file to reverse the masks. It takes a single argument that is the path to the folder where the dataset is stored.
```bash
python black_and_white_reverse_all.py --folder <path_to_directory>
```


## Achknowledgements

For the creation of the 3D scenes and the generation of the data, the following assets were used:

* **Water**
  * StylizedWater2 by [STAGGART Creation](https://staggart.xyz/unity/stylized-water-2/sws-2-docs/) [[Unity Asset Store](https://assetstore.unity.com/packages/vfx/shaders/stylized-water-2-170386?aid=1011l7Uk8&pubref=website&utm_campaign=unity_affiliate&utm_medium=affiliate&utm_source=partnerize-linkmaker)] 

* **1_CityScene**
  * Fantastic City Generator by MasterPixel3D [[Unity Asset Store](https://assetstore.unity.com/packages/3d/environments/urban/fantastic-city-generator-157625)] 

* **2_ForestScene, 3_ForestSceneWaterfalls**
  * Forest Environment - Dynamic Nature by NatureManufacture [[Unity Asset Store](https://assetstore.unity.com/packages/3d/vegetation/forest-environment-dynamic-nature-150668)]

* **4_LakeDamScene**
  * "Hampton Lake Dam [Post Hurricane Irma](https://skfb.ly/6BFWo)"  by likeonions is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).

* **5_ SnowScene**
  * "Icy Terrain Export" (https://skfb.ly/6XrFQ) by josevega is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).
  * Free Snow Mountain, ProAssets [Unity Asset Store](https://assetstore.unity.com/packages/3d/environments/landscapes/free-snow-mountain-63002)

* **6_CityBridgeScene, 7_CityBridgeSceneFlooded**
  * "Modern City Block" (https://skfb.ly/6V8Rx) by akselmot is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).

* **8_bridge_night_scene**
  * "Bridge Over Tunnel" (https://skfb.ly/osKXq) by jimbogies is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).
  * StreetLamps by SpaceZeta https://assetstore.unity.com/packages/3d/props/exterior/street-lamps-165658
  * Real New York City Vol. 2 by Geopipe, Inc. https://assetstore.unity.com/packages/3d/environments/urban/real-new-york-city-vol-2-222827
  * Tileable Bricks Wall by Game-Ready Studios https://assetstore.unity.com/packages/2d/textures-materials/brick/tileable-bricks-wall-24530

* **9_RiverScene**
  * "Terrain" (https://skfb.ly/o8ZQy) by FNG is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).

* **10_CityFloodedScene**
  * "CCity Building Set 1" (https://skfb.ly/LpSC) by Neberkenezer is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).
  * "The Dead Sea chalet, Jordan" (https://skfb.ly/owRFu) by mas.office.jo is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/).

* **11_TerrainScene**
  * Unity Terrain - URP Demo Scene, Unity Technologies [[Unity Asset Store](https://assetstore.unity.com/packages/3d/environments/unity-terrain-urp-demo-scene-213197)]


	
* **Other**
	* RaindropFX Pro URP, HZT [[Unity Asset Store](https://assetstore.unity.com/packages/vfx/shaders/fullscreen-camera-effects/raindropfx-pro-urp-215232)]
	* Terrain to Mesh, Amazing Assets [[Unity Asset Store](https://assetstore.unity.com/packages/tools/terrain/terrain-to-mesh-195349)]
	* Terrain to OBJ, Amazing Assets [[Unity Asset Store](https://assetstore.unity.com/packages/tools/terrain/terrain-to-obj-170663)]
  * Skybox Materials: Sunrise - Sunset - Night - HDRIs - 4k, HDRI Haven [[Unity Asset Store](https://assetstore.unity.com/packages/2d/textures-materials/sunrise-sunset-night-hdris-4k-178134)]



## Notes

* **`ForestSceneWaterfalls`**
    * Water reflection: Reflection of the surroundsing on the water's surface is not visible because of the nature of the water bodies. This scene includes running/falling water.
    * Binary masks: The Planar Reflection Renderer is not used, therefore the binary masks are in the correct form (water: white, background: black).


* **`SnowScene`**:
    * SnowScene_BuildV1: The water's surface is kept smooth to resemble a snow landscape.
    * SnowScene_BuildV2: The normal map's intensity applied to the water is increased to become slightly rough, so that it resembles a water body in all randomization settings.



## Development
* Unity 2021.3.11f1
* [Universal Rendering Pipeline (URP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.1/manual/index.html) 12.1.7
* Unity Perception 0.11.2-preview.2