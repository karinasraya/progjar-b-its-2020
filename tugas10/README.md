# Tugas 10
## Menjalankan Program
* Jalankan async_server.py pada port 9002, 9003, 9004, 9005 dengan cara menjalankan runserver.sh

![alt text](Capture/run_server.JPG)

* Jalankan lb.py pada port 44444
* Jalankan browser, akseslah http://localhost:44444/page.html

![alt text](Capture/browser.JPG)

* Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian

![alt text](Capture/log_program.JPG)
#
## Tabel performance test dapat dilihat pada file 05111740000003_Tugas10.pdf atau pada lampiran berikut ini
* Asyncronus Server

![alt text](Capture/Tabel1.JPG)

* Multithread Server

![alt text](Capture/Tabel2.JPG)

* Asyncronus Server Dengan Load Balancer

![alt text](Capture/Tabel3.JPG)