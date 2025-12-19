from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer


class CourseViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        courses = Course.objects.all()
        data = [
            {"id": str(c.id), "name": c.name, "duration": c.duration}
            for c in courses
        ]
        return Response(data)

    def create(self, request):
        if not request.user.groups.filter(name="Admin").exists():
            return Response({"error": "Only Admin can create courses"}, status=403)

        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course(**serializer.validated_data).save()
        return Response(
            {"id": str(course.id), **serializer.validated_data},
            status=201
        )


class StudentViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        students = Student.objects.all()
        data = [
            {
                "id": str(s.id),
                "name": s.name,
                "age": s.age,
                "course": str(s.course.id) if s.course else None
            }
            for s in students
        ]
        return Response(data)

    def create(self, request):
        if not request.user.groups.filter(name="Admin").exists():
            return Response({"error": "Only Admin can add students"}, status=403)

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = Course.objects.get(id=serializer.validated_data["course"])

        student = Student(
            name=serializer.validated_data["name"],
            age=serializer.validated_data["age"],
            course=course
        ).save()

        return Response(
            {
                "id": str(student.id),
                "name": student.name,
                "age": student.age,
                "course": str(course.id)
            },
            status=201
        )
