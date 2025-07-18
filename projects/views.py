from django.shortcuts import render, get_object_or_404
from .models import Project, Department
from django.db.utils import OperationalError
from django.db.models import Count

def ensure_departments():
    department_names = [
        "Computer Science Engineering (CSE)",
        "Information Technology (IT)",
        "Electronics and Communication (ECE)",
        "Electrical and Electronics (EEE)",
        "Mechanical Engineering (ME)",
        "Civil Engineering (CE)",
        "Chemical Engineering",
        "Automobile Engineering",
        "Instrumentation Engineering",
        "Aerospace Engineering",
        "Mechatronics",
        "Biomedical Engineering",
        "Marine Engineering",
        "Mining Engineering",
        "Petroleum Engineering",
        "Industrial Engineering",
    ]
    for name in department_names:
        Department.objects.get_or_create(name=name)

def ensure_example_projects():
    try:
        ensure_departments()
        if Project.objects.count() == 0:
            # Map department names to Department objects
            depts = {d.name: d for d in Department.objects.all()}
            Project.objects.create(
                title="AI Chess Analyzer",
                student_name="Alice Smith",
                department=depts["Computer Science Engineering (CSE)"],
                short_description="A tool to analyze chess games using AI.",
                full_description="This project uses machine learning to analyze chess games and suggest improvements.",
                github_or_demo_link="https://github.com/example/chess-analyzer"
            )
            Project.objects.create(
                title="Smart Campus App",
                student_name="John Doe",
                department=depts["Information Technology (IT)"],
                short_description="A mobile app for campus navigation and events.",
                full_description="An IT project to help students navigate campus and stay updated on events.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="IoT Home Automation",
                student_name="Priya Kumar",
                department=depts["Electronics and Communication (ECE)"],
                short_description="Automate home appliances using IoT.",
                full_description="A system to control home appliances remotely using IoT and communication protocols.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Smart Energy Meter",
                student_name="Rahul Singh",
                department=depts["Electrical and Electronics (EEE)"],
                short_description="Monitor and manage energy usage.",
                full_description="A smart meter to track and optimize household energy consumption.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="3D Printed Engine Parts",
                student_name="Meera Patel",
                department=depts["Mechanical Engineering (ME)"],
                short_description="Using 3D printing for engine prototyping.",
                full_description="Mechanical project on rapid prototyping of engine parts using 3D printing.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Earthquake Resistant Building Model",
                student_name="Suresh Reddy",
                department=depts["Civil Engineering (CE)"],
                short_description="A model for earthquake-resistant structures.",
                full_description="Civil project focusing on innovative building designs to withstand earthquakes.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Biofuel Production from Algae",
                student_name="Ananya Roy",
                department=depts["Chemical Engineering"],
                short_description="Producing biofuel using algae.",
                full_description="Chemical engineering project on sustainable biofuel production from algae.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Hybrid Electric Vehicle Design",
                student_name="Vikram Chauhan",
                department=depts["Automobile Engineering"],
                short_description="Designing a hybrid electric vehicle.",
                full_description="Automobile project on the design and simulation of a hybrid electric vehicle.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Smart Sensor Calibration System",
                student_name="Divya Sharma",
                department=depts["Instrumentation Engineering"],
                short_description="Automated calibration for industrial sensors.",
                full_description="Instrumentation project for developing a smart calibration system for sensors.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Miniature Drone for Surveillance",
                student_name="Arjun Nair",
                department=depts["Aerospace Engineering"],
                short_description="A small drone for aerial surveillance.",
                full_description="Aerospace project on the design and control of a miniature surveillance drone.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Robotic Arm for Assembly Line",
                student_name="Sneha Gupta",
                department=depts["Mechatronics"],
                short_description="A robotic arm for industrial automation.",
                full_description="Mechatronics project on building a programmable robotic arm for assembly lines.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Wearable Health Monitor",
                student_name="Rohan Mehta",
                department=depts["Biomedical Engineering"],
                short_description="A wearable device for health monitoring.",
                full_description="Biomedical project on a wearable device to monitor vital health parameters.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Autonomous Underwater Vehicle",
                student_name="Lakshmi Menon",
                department=depts["Marine Engineering"],
                short_description="AUV for underwater exploration.",
                full_description="Marine engineering project on the design of an autonomous underwater vehicle.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Mine Safety Monitoring System",
                student_name="Amitabh Das",
                department=depts["Mining Engineering"],
                short_description="A system to monitor mine safety.",
                full_description="Mining engineering project for real-time safety monitoring in mines.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Enhanced Oil Recovery Techniques",
                student_name="Fatima Sheikh",
                department=depts["Petroleum Engineering"],
                short_description="Techniques for improved oil recovery.",
                full_description="Petroleum engineering project on advanced methods for oil extraction.",
                github_or_demo_link=""
            )
            Project.objects.create(
                title="Smart Manufacturing Dashboard",
                student_name="Karthik Iyer",
                department=depts["Industrial Engineering"],
                short_description="Dashboard for monitoring manufacturing KPIs.",
                full_description="Industrial engineering project on a smart dashboard for real-time manufacturing analytics.",
                github_or_demo_link=""
            )
    except OperationalError:
        pass  # Database might not be migrated yet

def department_list(request):
    ensure_example_projects()
    departments = Department.objects.all().annotate(num_projects=Count('projects')).order_by('name')
    return render(request, 'projects/department_list.html', {'departments': departments})

def department_projects(request, department_name):
    department = get_object_or_404(Department, name=department_name)
    projects = department.projects.all().select_related('department')
    return render(request, 'projects/department_projects.html', {'projects': projects, 'department': department.name})

def project_detail(request, pk):
    project = get_object_or_404(Project.objects.select_related('department'), pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
