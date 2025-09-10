ENVNAME=$1
PYTHONVERSION=${2:-3.10}
KEEP=${3:-false}

# Create conda environment
echo "Creating conda environment $ENVNAME with Python $PYTHONVERSION"
conda create -n $ENVNAME python=$PYTHONVERSION -y

# Create .envrc file with the environment name
echo "Creating .envrc file with the environment name"
cat <<EOF > .envrc
# Python environment
conda activate $ENVNAME
EOF

# Allow direnv to manage the environment
echo "Allowing direnv to manage the environment"
direnv allow

# Remove the script
if [ "$KEEP" = false ]; then
    echo "Removing the script"
    rm create_python_environment.sh
fi

conda activate $ENVNAME