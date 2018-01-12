from util.project_information import ProjectInformation


def init_project(args):
    project = ProjectInformation(args)
    project.init_project()
