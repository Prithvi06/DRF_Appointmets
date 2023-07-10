from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from doctor.models import DoctorProfile
from accounts.models import UserAccount

from datetime import datetime
from io import StringIO, BytesIO
from PIL import Image
from django.core.files.base import ContentFile
import os
from project.settings.base import MEDIA_ROOT
class BaseTestCase(TestCase):

	def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
		"""
		Generate a test image, returning the filename that it was saved as.

		If ``storage`` is ``None``, the BytesIO containing the image data
		will be passed instead.
		"""
		# import pdb;pdb.set_trace()
		image_file = BytesIO()
		image = Image.new('RGBA', size=(50,50), color=(256,0,0))
		image.save(image_file, 'png')
		image_file.name = 'test.png'
		image_file.seek(0)

		return image_file#ContentFile(image_file.read(), 'test.png')

	def create_user(self, **kwargs):
		return UserAccount.objects.create(**kwargs)

	def create_doctor_profile(self, **kwargs):
		return DoctorProfile.objects.create(**kwargs)

	def setUp(self):
		self.email = "testdoctor@gmail.com"
		self.user_data = {
			'role': UserAccount.DOCTOR,
			'email': self.email,
			'name': 'John',
			'email_otp': '12345',
			'mobile_no': '9977665544',
			'last_name': 'Doe',
			'is_staff': False,
			'is_superuser': False,
			'is_active': True,
			'is_email_verified': False,
			'device_id': '1',
			'password': 'test@123'
		}
		self.user = self.create_user(**self.user_data)

		self.specialty = 'Pathologist'
		self.career_started = datetime.today().date()
		self.city = 'Indore'
		self.locality = 'bengali square'
		self.clinic = 'Hansraj Clinic'
		self.fees = 500
		self.expertise_area = 'Expert in Diagnosing Disease of particular patient'
		
		avatar = self.create_image(None, 'avatar.png')
		avatar_file = SimpleUploadedFile('test_front.png', avatar.getvalue())
		self.doctor_profile_data = {
			'doctor': self.user,
			'doctor_pic': avatar_file,#SimpleUploadedFile(name='dummy_pic.jpg', content=b'', content_type='image/jpeg'),
			'gender': DoctorProfile.MALE,
			'career_started': self.career_started,
			'specialty' : self.specialty,
			'city': self.city,
			'locality':self.locality,
			'clinic': self.clinic,
			'consultation_fees': self.fees,
			'expertise_area': self.expertise_area,
			'verification': DoctorProfile.INCOMPLETED
		}
		self.doctor_profile = self.create_doctor_profile(**self.doctor_profile_data)


class DoctorProfileTestCase(BaseTestCase):

	def test_doctor_profile_object_created(self):
		doctor_profile = DoctorProfile.objects.all()
		self.assertEqual(doctor_profile.count(), 1)

	def test_doctor_image_field_value(self):
		import pdb;pdb.set_trace()
		doctor_profile = DoctorProfile.objects.all().first()
		self.assertEqual(doctor_profile.doctor_pic.name[-4:], ".png")

	def tearDown(self):
		# import pdb;pdb.set_trace()
		images_path = os.path.join(MEDIA_ROOT, 'images')
		files = [i for i in os.listdir(images_path) 
				if os.path.isfile(os.path.join(images_path, i))
				and i.startswith('test_')]

		for file in files:
			os.remove(os.path.join(images_path, file))