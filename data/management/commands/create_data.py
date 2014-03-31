import datetime
import random

from django.core.management.base import BaseCommand, CommandError

from data.models import *
from master.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.data_country()
        self.data_city()
        self.data_hospital()
        self.data_category_specialist()
        self.data_sub_category()
        self.data_dokter_boromeus()

    def data_country(self):
        print '=============== Creating Data country'
        country_data = [
            ('Indonesia','Indonesia'), ('Malaysia','Malaysia'),
            ('Singapore','Singapore'), ('Vietnam','Vietnam'),
            ('Philipines','Philipines'), ('Thailand','Thailand'),
            ('Burma','Burma')]

        try:
            for i in country_data:
                data = Country.objects.get_or_create(
                    name = i[0],
                    description = i[1]
                )
                print 'create country : %s ' % i[0]
        except Exception, e:
            print 'FAILED create country : %s ERROR : %s' % (i[0], e)


    def data_city(self):
        print '=============== Creating Data city'
        city_data = [
            ('Jakarta', 'Jakarta'), ('Bandung', 'Bandung'),
            ('Yogyakarta', 'Yogyakarta'), ('Surabaya', 'Surabaya'),
            ('Denpasar', 'Denpasar')]

        try:
            country = Country.objects.get(name="Indonesia")
            for i in city_data:
                data = City.objects.get_or_create(
                    name = i[0],
                    description = i[1],
                    country=country
                )
                print 'create city : %s ' % i[0]
        except Exception, e:
            print 'FAILED create city : %s  ERROR : %s' % (i[0], e)


    def data_hospital(self):
        bandung_hospital = [
            ('RS Advent', 'Jl. Cihampelas No 161', '(022) 2034386', 'rs_1.jpg'),
            ('RS Umum Pusat Hasan Sadikin', 'Jl. Pasteur No 38', '(022) 2034953', 'rs_2.jpg'),
            ('RS Santo Yusup', 'Jl. Cikutra No 7', '(022) 7208172', 'rs_3.jpg'),
            ('RS Santo Borromeus', 'Jl. Ir H Juanda No 100', '(022) 255200', 'rs_4.jpg'),
            ('RS Immanuel', 'Jl. Kopo No 161', '(022) 5201656', 'rs_5.jpg'),
            ('RS Mitra Kasih', 'Jl. Raya Cibabat No 341', '(022) 6654852', 'rs_6.jpg'),
            ('RS Pindad', 'Jl. Gatot Subroto No 517', '(022) 7321964', 'rs_7.jpg')
        ]

        print '=============== Creating Data for BANDUNG'
        try:
            bd = City.objects.get(name='Bandung')
            for i in bandung_hospital:
                data = Hospital.objects.get_or_create(
                    name = i[0], address = i[1],
                    phone = i[2], image = i[3], city=bd
                )
                print 'create hospital : %s (city : %s)' % (i[0], bd)
        except Exception, e:
            print 'FAILED create hospital : %s  ERROR : %s' % (i[0], e)

        jakarta_hospital = [
            ('RS Royal Taruma', 'Jl. Daan Mogot No.34 Grogol', '(021) 56958338', 'rs_8.jpg'),
            ('RS Siloam Graha Medika', 'Jl. Raya Perjuangan Kav. 8 Kebon Jeruk', '(021) 5300888', 'rs_9.jpg'),
            ('RS Pelni Petamburan', 'Jl. K. S. Tubun No. 92 - 94', '(021) 5306901', 'rs_10.jpg'),
            ('RSIA Hermina Daan Mogot', 'Jl. Kintamani Raya No. 2 Perumahan Daan Mogot', '(020212) 5408989', 'rs_11.jpg'),
            ('RS Sumber Waras', 'Jl. Kyai Tapa No. 1 Grogol', '(021) 5682011', 'rs_12.jpg'),
            ('RS Puri Mandiri Kedoya', 'Jl. Kedoya Raya No.2', '(021) 5828299', 'rs_13.jpg')
        ]
        print '=============== Creating Data for JAKARTA'
        try:
            jt = City.objects.get(name='Jakarta')
            for i in jakarta_hospital:
                data = Hospital.objects.get_or_create(
                    name = i[0], address = i[1],
                    phone = i[2], image = i[3], city=jt
                )
                print 'create hospital : %s (city : %s)' % (i[0], jt)
        except Exception, e:
            print 'FAILED create hospital : %s  ERROR : %s' % (i[0], e)

        print '=============== Creating Data for JOGJA'
        jogja_hospital = [
            ('RS Dr.Sardjito', 'Jl Kesehatan 1', '(0274) 587333', 'rs_14.jpg'),
            ('RS Bethesda', 'Jl Jend Sudirman 70', '(0274) 55224', 'rs_15.jpg'),
            ('RS Panti Rapih', 'Jl Teuku Cik Ditiro 30', '(0274) 514845', 'rs_16.jpg'),
            ('RS Jojga International', 'Jl Ring Road Utara No. 160', '(0274) 4463-555', 'rs_17.jpg'),

        ]
        try:
            jt = City.objects.get(name='Yogyakarta')
            for i in jogja_hospital:
                data = Hospital.objects.get_or_create(
                    name = i[0], address = i[1],
                    phone = i[2], image = i[3], city=jt
                )
                print 'create hospital : %s (city : %s)' % (i[0], jt)
        except Exception, e:
            print 'FAILED create hospital : %s  ERROR : %s' % (i[0], e)


    def data_category_specialist(self):
        category_specialist = [
            ('Klinik Bedah', 'Klinik Bedah'),
            ('Klinik Gigi', 'Klinik Gigi'),
            ('Klinik Anak', 'Klinik Anak'),
            ('Klinik Penyakit Dalam', 'Klinik Penyakit Dalam'),
            ('Klinik Psikologi', 'Klinik Psikologi'),
            ('Klinik Umum', 'Klinik Umum')
        ]

        print '=============== Creating Data Category Specialist'
        try:
            for i in category_specialist:
                data = CategorySpecialist.objects.get_or_create(
                    name = i[0],
                    description = i[1]
                )
                print 'create Category Specialist : %s ' % i[0]
        except Exception, e:
            print 'FAILED Category Specialist : %s ERROR : %s' % (i[0], e)

    def data_sub_category(self):
        def insert_data(name=None, desc=None, klinik=None):
            try:
                sp = CategorySpecialist.objects.get(name=klinik)
                sub = Specialist.objects.get_or_create(
                    name = name, description = desc, category = sp
                )
                print 'create Sub Specialist : %s (%s) ' % (name, sp)
            except Exception, e:
                print 'FAILED Sub Specialist : %s ERROR : %s' % (name, e)

        print '=============== Creating Data sub Specialist'
        data_bedah = [
            ('Dokter Bedah Anak', 'Dokter Bedah Bedah Anak'),
            ('Dokter Bedah Digestif', 'Dokter Bedah Digestif'),
            ('Dokter Bedah Mulut', 'Dokter Bedah Mulut'),
            ('Dokter Bedah Plastik', 'Dokter Bedah Plastik'),
            ('Dokter Bedah Saraf', 'Dokter Bedah Saraf'),
            ('Dokter Bedah Umum', 'Dokter Bedah Umum'),
            ('Dokter Bedah Urologi', 'Dokter Bedah Urologi'),
        ]
        for i in data_bedah:
            insert_data(i[0], i[1], 'Klinik Bedah')

        data_gigi = [
            ('Dokter Gigi', 'Dokter Gigi'),
            ('Dokter Gigi Anak', 'Dokter Gigi Anak'),
            ('Dokter Gigi Endodontik', 'Dokter Gigi Endodontik'),
            ('Dokter Gigi Orthodontik', 'Dokter Gigi Orthodontik')
        ]
        for i in data_gigi:
            insert_data(i[0], i[1], 'Klinik Gigi')

        data_anak = [
            ('Dokter Hematologi Anak', 'Dokter Hematologi Anak'),
            ('Dokter Fisioterapi Anak', 'Dokter Fisioterapi Anak'),
            ('Dokter THT Anak', 'Dokter THT Anak')
        ]
        for i in data_anak:
            insert_data(i[0], i[1], 'Klinik Anak')

        data_penyakit_dalam = [
            ('Dokter THT', 'Dokter THT'),
            ('Dokter Jantung', 'Dokter Jantung'),
            ('Dokter Penyakit Dalam', 'Dokter Penyakit Dalam'),
            ('Dokter Saraf', 'Dokter Saraf')
        ]
        for i in data_penyakit_dalam:
            insert_data(i[0], i[1], 'Klinik Penyakit Dalam')

        data_psikologi = [
            ('Dokter Psikologi', 'Dokter Psikologi'),
            ('Dokter Psikologi Anak', 'Dokter Psikologi Anak')
        ]
        for i in data_psikologi:
            insert_data(i[0], i[1], 'Klinik Psikologi')

        data_umum = [
            ('Dokter Umum', 'Dokter Umum')
        ]
        for i in data_umum:
            insert_data(i[0], i[1], 'Klinik Umum')

    def data_dokter_boromeus(self):
        def insert_data(name=None, gender=None, specialist=None, image=None, day=None, hours=None):

            try:
                phone_fake = [str(random.randint(0,9)) for count in range(13)]
                phone = "%s%s" % ('+628', ''.join(phone_fake))

                hospital = Hospital.objects.get(name='RS Santo Borromeus')
                sp = Specialist.objects.get(name=specialist)
                quota = 20

                doc, created = Doctor.objects.get_or_create(
                    name = name, phone = phone,
                    gender = gender, hospital = hospital,
                    specialist = sp, is_active = True,
                    #date_created = datetime.datetime.utcnow(),
                    image = image, patient_quota = quota
                )
                for i in day:
                    sch = DoctorSchedule.objects.get_or_create(
                        hospital = hospital, doctor = doc,
                        days = int(i), hours = hours, patient_quota = quota
                    )
                    print 'create schedule Dokter : %s day : %s' % (name, i)

            except Exception, e:
                print 'FAILED create dokter : %s ERROR : %s' % (name, e)

        doc_pnykit_dalam = [
            ('dr. Dian Yudhatama , SpPD.', 2, 'Dokter Penyakit Dalam', 'doc_1.jpg', [1,2,3,4,5,6], '08.00 - 13.30'),
            ('dr. Edwin Setiabudi , SpPD.', 1, 'Dokter Penyakit Dalam', 'doc_2.jpg', [1,4,6], '18.30 - 19.30'),
            ('dr. Handoko , SpPD.', 1, 'Dokter Penyakit Dalam', 'doc_3.jpg', [1,2,5,6], '08.00 - 14.00'),
            ('dr. Jefry Tahari , SpPD.', 1, 'Dokter Penyakit Dalam', 'doc_4.jpg', [1,2,3,4,5,6], '10.00 - 14.00'),
            ('dr. Mukta Prawata , SpPD.', 1, 'Dokter Penyakit Dalam', 'doc_5.jpg', [1,2,3,4,5,6], '08.30 - 13.30'),
            ('dr. Ni Nyoman Ati S , SpPD.', 2, 'Dokter Penyakit Dalam', 'doc_6.jpg', [1,4,6], '14.30 - 18.00'),
            ('dr. Veronica Dhian R , SpPD.', 2, 'Dokter Penyakit Dalam', 'doc_7.jpg', [2,5], '18.30 - 19.30'),
            ('dr. Widyastuti Amidjojo', 2, 'Dokter Penyakit Dalam', 'doc_8.jpg', [1,2,3,4,5,6], '11.00 - 13.30')
        ]

        for i in doc_pnykit_dalam:
            insert_data(i[0], i[1], i[2], i[3], i[4], i[5])

        doc_tht= [
            ('dr. Bogi Suseno , SpTHT', 1, 'Dokter THT', 'doc_9.jpg', [1,2,6,7], '12.00 - 17.00'),
            ('dr. Langlang Dogha , M.Kes', 1, 'Dokter THT', 'doc_10.jpg', [5], '15.00 - 16.00'),
            ('dr. Nur Akbar Aroeman , SpTHT.', 1, 'Dokter THT', 'doc_11.jpg', [1,2,5,6], '16.00 - 18.00'),
            ('dr. Shinta Nurmasari , M.Kes,SpTHT', 2, 'Dokter THT', 'doc_12.jpg', [1,2,3,5], '08.00 - 11.00'),
            ('dr. Suparti Suleh , SpTHT.', 1, 'Dokter THT', 'doc_13.jpg', [3,4,6], '08.00 - 11.00'),
        ]

        for i in doc_tht:
            insert_data(i[0], i[1], i[2], i[3], i[4], i[5])

