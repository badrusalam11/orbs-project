from orbs.runner import Runner

def run():
    runner = Runner()
    runner.run_feature("include/features/login_cura.feature")
