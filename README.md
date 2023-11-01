# HandAirGesture

Using Hand landmarks legacy as well as upgraded solutions provided by Mediapipe to control mouse cursor, credited to Viet Nguyen @uvipen

Legacy Solutions work quite well. However with Upgraded version, I encounter an issue where it seems to be a known issue in Windows related to 'pyyaml' and 'tf datasets' versions, which in turn make pip looking at multiple versions of mediapipe-model-maker to determine which version is compatible with other requirements, and in the end unable to resolve the issue.

Solution log using Windows Subsystem for Linux(WSL):

- Step 1: install wsl:

  https://learn.microsoft.com/en-us/windows/wsl/install

- Step 2: install cuda:

  wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin

  sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600

  wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb

  sudo dpkg -i cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb

  sudo cp /var/cuda-repo-wsl-ubuntu-11-8-local/cuda-\*-keyring.gpg /usr/share/keyrings/

  sudo apt-get update

  sudo apt-get -y install cuda

- Step 3: install cudnn:

  sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.5.29_1.0-1_amd64.deb

  sudo cp /var/cudnn-local-repo-ubuntu2204-8.9.5.29/cudnn-local-\*-keyring.gpg /usr/share/keyrings/

  sudo apt-get update

  sudo apt -y install libcudnn8 libcudnn8-dev

- Step 4: install mediapipe:

  pip install mediapipe-model-maker==0.2.1.3
