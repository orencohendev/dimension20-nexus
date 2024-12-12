

# actions to run, type, lint, test, build, deploy, clean
type:
	@echo "Type checking..."
	@poetry run mypy src

lint:
	@echo "Linting..."
	@poetry run black src --check

lint_fix:
	@echo "Linting and fixing..."
	@poetry run black src 

start:
	@echo "Running..."
	cd src && poetry run python -m app.app

test:
	@echo "Testing..."
	@poetry run pytest src/tests