# pydanfossair
Python module and client for Danfoss Air HRV systems. 

## Usage
### Read all commands
	python -m pydanfossair --host IP_ADDRESS

### Send update command
	python -m pydanfossair --host IP_ADDRESS --command COMMAND

## Supported commands
- boost_on
- boost_off
- bypass_on
- bypass_off
- automatic_bypass_on
- automatic_bypass_off
