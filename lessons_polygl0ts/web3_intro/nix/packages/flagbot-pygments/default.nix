{
  inputs,
  python3Packages,
  ...
}:
python3Packages.buildPythonPackage {
  pname = "pygments-flagbot";
  version = "0.0.1";
  src = inputs.flagbot-pygments;
  buildInputs = [python3Packages.pygments];
}
