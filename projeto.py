# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projeto.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from scipy.integrate import odeint
import numpy as np
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 727)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(460, 490, 121, 31))
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_ana = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ana.setGeometry(QtCore.QRect(460, 530, 121, 31))
        self.pushButton_ana.setObjectName("pushButton_ana")
        self.textEdit_41 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_41.setGeometry(QtCore.QRect(160, 560, 61, 25))
        self.textEdit_41.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_41.setObjectName("textEdit_41")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 560, 121, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 590, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 530, 131, 16))
        self.label_16.setObjectName("label_16")
        self.textEdit_42 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_42.setGeometry(QtCore.QRect(160, 590, 61, 25))
        self.textEdit_42.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_42.setObjectName("textEdit_42")
        self.textEdit_43 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_43.setGeometry(QtCore.QRect(160, 620, 61, 25))
        self.textEdit_43.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_43.setObjectName("textEdit_43")
        self.textEdit_44 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_44.setGeometry(QtCore.QRect(160, 650, 61, 25))
        self.textEdit_44.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_44.setObjectName("textEdit_44")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(10, 620, 141, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(10, 650, 131, 16))
        self.label_25.setObjectName("label_25")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 661, 461))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_45 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_45.setGeometry(QtCore.QRect(290, 630, 41, 25))
        self.textEdit_45.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_45.setObjectName("textEdit_45")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(250, 500, 31, 16))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(10, 500, 121, 16))
        self.label_28.setObjectName("label_28")
        self.textEdit_46 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_46.setGeometry(QtCore.QRect(290, 500, 41, 25))
        self.textEdit_46.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_46.setObjectName("textEdit_46")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(240, 630, 91, 16))
        self.label_32.setObjectName("label_32")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(470, 570, 221, 16))
        self.label_29.setObjectName("label_29")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(470, 590, 201, 16))
        self.label_58.setObjectName("label_58")
        self.textEdit_48 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_48.setGeometry(QtCore.QRect(160, 500, 61, 25))
        self.textEdit_48.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_48.setObjectName("textEdit_48")
        self.textEdit_49 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_49.setGeometry(QtCore.QRect(160, 530, 61, 25))
        self.textEdit_49.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_49.setObjectName("textEdit_49")
        self.textEdit_50 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_50.setGeometry(QtCore.QRect(290, 530, 41, 25))
        self.textEdit_50.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_50.setObjectName("textEdit_50")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(250, 530, 31, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(250, 560, 31, 16))
        self.label_35.setObjectName("label_35")
        self.textEdit_51 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_51.setGeometry(QtCore.QRect(290, 560, 41, 25))
        self.textEdit_51.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_51.setObjectName("textEdit_51")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(250, 590, 31, 16))
        self.label_36.setObjectName("label_36")
        self.textEdit_52 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_52.setGeometry(QtCore.QRect(290, 590, 41, 25))
        self.textEdit_52.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_52.setObjectName("textEdit_52")
        self.textEdit_53 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_53.setGeometry(QtCore.QRect(340, 500, 41, 25))
        self.textEdit_53.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_53.setObjectName("textEdit_53")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(470, 610, 221, 16))
        self.label_30.setObjectName("label_30")
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        self.label_59.setGeometry(QtCore.QRect(470, 630, 271, 16))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.centralwidget)
        self.label_60.setGeometry(QtCore.QRect(470, 650, 201, 16))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.centralwidget)
        self.label_61.setGeometry(QtCore.QRect(470, 670, 201, 16))
        self.label_61.setObjectName("label_61")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plotFigLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.plot_static_canvas = FigureCanvas(Figure(figsize=(2, 2)))
        self.plotFigLayout.addWidget(self.plot_static_canvas)

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        self.pushButton_input.clicked.connect(lambda:self.creat('GT'))
        self.pushButton_ana.clicked.connect(lambda:self.creat('TRA'))

    def creat(self,aaa):
        if True:
            if True:
                try: 
                    self.nodo = float(self.textEdit_48.toPlainText())
                except : 
                    self.nodo =0
                    self.textEdit_48.insertPlainText(str(self.nodo))
                try: 
                    self.semieixo = float(self.textEdit_49.toPlainText())
                except : 
                    self.semieixo = 42500
                    self.textEdit_49.insertPlainText(str(self.semieixo))
                try: 
                    self.exce = float(self.textEdit_41.toPlainText())
                except : 
                    self.exce = 0
                    self.textEdit_41.insertPlainText(str(self.exce))
                try: 
                    self.argperi = float(self.textEdit_42.toPlainText())
                except : 
                    self.argperi = 0
                    self.textEdit_42.insertPlainText(str(self.argperi))
                try: 
                    self.anaved = float(self.textEdit_43.toPlainText())
                except : 
                    self.anaved = 0
                    self.textEdit_43.insertPlainText(str(self.anaved))

                try: 
                    self.inclina = float(self.textEdit_44.toPlainText())
                except : 
                    self.inclina = 0
                    self.textEdit_44.insertPlainText(str(self.inclina))

                try: 
                    self.periodos = float(self.textEdit_45.toPlainText())
                except : 
                    self.periodos = 1
                    self.textEdit_45.insertPlainText(str(self.periodos))

                try: 
                    self.hora = float(self.textEdit_46.toPlainText())
                except : 
                    self.hora = 0
                    self.textEdit_46.insertPlainText(str(self.hora))

                try: 
                    self.min = float(self.textEdit_53.toPlainText())
                except : 
                    self.min = 0
                    self.textEdit_53.insertPlainText(str(self.min))  
                try: 
                    self.dia = float(self.textEdit_50.toPlainText())
                except : 
                    self.dia = 11
                    self.textEdit_50.insertPlainText(str(self.dia)) 

                try: 
                    self.mes = float(self.textEdit_51.toPlainText())
                except : 
                    self.mes = 9
                    self.textEdit_51.insertPlainText(str(self.mes)) 

                try: 
                    self.ano = float(self.textEdit_52.toPlainText())
                except : 
                    self.ano = 2006
                    self.textEdit_52.insertPlainText(str(self.ano))                                      


        self.plot(aaa)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_input.setText(_translate("MainWindow", "Ground Track"))
        self.pushButton_ana.setText(_translate("MainWindow", "Trgetória"))
        self.label_14.setText(_translate("MainWindow", "Excentricidade (º)"))
        self.label_15.setText(_translate("MainWindow", "Argumento do perigeo (º)"))
        self.label_16.setText(_translate("MainWindow", "Semi-eixo maior (km)"))
        self.label_24.setText(_translate("MainWindow", "Anomalia verdadeira (º)"))
        self.label_25.setText(_translate("MainWindow", "Inclinação (º)"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot"))
        self.label_26.setText(_translate("MainWindow", "Hora"))
        self.label_28.setText(_translate("MainWindow", "Nodo ascendente (º)"))
        self.label_32.setText(_translate("MainWindow", "Períodos"))
        self.label_29.setText(_translate("MainWindow", "Desenvolvido por:"))
        self.label_58.setText(_translate("MainWindow", "Geraldo Majella N. Junior "))
        self.label_34.setText(_translate("MainWindow", "Dia"))
        self.label_35.setText(_translate("MainWindow", "Mês"))
        self.label_36.setText(_translate("MainWindow", "Ano"))
        self.label_30.setText(_translate("MainWindow", "Gabriel H. Barros Vieira"))
        self.label_59.setText(_translate("MainWindow", "Email de contato: "))
        self.label_60.setText(_translate("MainWindow", "thiacene@gmail.com"))
        self.label_61.setText(_translate("MainWindow", "ghomerob@gmail.com"))

    def haroldopetista(self,x,t):

        mi = 3.986e5

        dx = [0,0,0,0,0,0]

        dx[0] = x[3]
        dx[1] = x[4]
        dx[2] = x[5]
        dx[3] = -mi*(x[0]/((x[0]**2 + x[1]**2 + x[2]**2)**(3/2)))
        dx[4] = -mi*(x[1]/((x[0]**2 + x[1]**2 + x[2]**2)**(3/2)))
        dx[5] = -mi*(x[2]/((x[0]**2 + x[1]**2 + x[2]**2)**(3/2)))
        return dx

    def artigo(self,aaa):

        mi = 3.986e5
        e = self.exce/57.2958
        i = self.inclina/57.2958
        omega = self.argperi/57.2958
        Omega = self.nodo/57.2958
        tetha = self.anaved/57.2958
        a = self.semieixo
        nP = self.periodos
        T = 2*np.pi/(np.sqrt(mi/a**3))
        n = 2*np.pi/T
        r = a*(1-e**2)/(1+e*np.cos(tetha))
        x = r*np.cos(tetha)
        y = r*np.sin(tetha)
        z = 0

        dot_x = -((n*a)/(np.sqrt(1-e**2)))*np.sin(tetha)
        dot_y = ((n*a)/(np.sqrt(1-e**2)))*(e+np.cos(tetha))
        dot_z = 0

        rot1 = [[np.cos(-omega), np.sin(-omega), 0], [-np.sin(-omega),np.cos(-omega),0],[0, 0,1]]
        rot2 = [[1, 0, 0],[0, np.cos(-i), np.sin(-i)],[0, -np.sin(-i), np.cos(-i)]]
        rot3 = [[np.cos(-Omega), np.sin(-Omega), 0],[-np.sin(-Omega), np.cos(-Omega), 0],[0, 0, 1]]

        M = np.dot(np.dot(rot3,rot2),rot1)

        R = np.dot([x, y, z],np.transpose(M))
        V = np.dot([dot_x, dot_y, dot_z],np.transpose(M))
        A=self.ano
        M=self.mes
        D=self.dia
        h=self.hora
        m=self.min
        s=0

        #R = [4890.7, -5224.8, -850.1]
        #V = [-1.4, -0.1 ,-7.3]
        #R = [10016.34, -17012.52, 7899.28]
        #V = [2.5, -1.05, 3.88]
        mi = 3.986e5

        v = np.linalg.norm(V)
        r = np.linalg.norm(R)

        N = 7000
        dt = nP*T/(N-1) 
        cond_inicial = [R[0], R[1], R[2], V[0], V[1], V[2]]
        homi=[]
        for i in range(N):
            homi.append(dt*(i+1))
        RR = odeint(self.haroldopetista,cond_inicial,homi)
        RR = np.array(RR)

        DJ_0 = 367*A - np.int(7*(A + np.int((M + 9)/12))/4) + np.int(275*M/9) + D + 1721013.5

        Ji = (DJ_0 - 2415020.0)/36525
        tetag0 = 99.69098329 + 36000.76893*Ji + (3.87080e-4)*(Ji**2)

        tetag0 = np.deg2rad(tetag0)
        aux = np.int(tetag0/(2*np.pi))
        tetag0 = tetag0 - (2*np.pi*aux)
        print(tetag0)
        lat=[]
        lon=[]
        for i in range(len(RR)):
            tetag = tetag0 + 0.00007272*dt*i
            SS = [RR[i,0], RR[i,1] ,RR[i,2]]
            lat.append(np.arcsin((RR[i,2]/np.linalg.norm(SS)))*57.2958)
            tetag=(tetag)
            tetag = ((tetag/360)- np.int(tetag/360))*360

            lon.append((np.arctan2(RR[i,1],RR[i,0])-tetag)*57.2958)
            while lon[i]<-180:
            #if lon[i]<-180:
                lon[i]=lon[i]+360
            while lon[i]>180:
            #if lon[i]<-180:
                lon[i]=lon[i]-360

        if aaa == 'GT':
            return lat, lon
        else:
            return RR




    def plot(self, aaa):
        #self.legonoff = self.checkBox.isChecked()
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure

        if aaa == 'GT':
            lat, lon = self.artigo(aaa)

            self.ax = self.fig.add_subplot(111)
            im = plt.imread('clecio.jpg')

            self.ax.imshow(im,extent=[-180, 180, -90, 90])
            self.ax.scatter(lon, lat,s=8,c='blue')
            self.ax.set_title('Ground Track')
            self.ax.set_xlabel('Latitude')
            self.ax.set_ylabel('Longitude')

        else:
            
            self.fig_canvas = self.plot_static_canvas
            self.fig = self.fig_canvas.figure
            self.ax = self.fig.add_subplot(111, projection='3d')

            RR = self.artigo(aaa)
            xline = RR[:,0]
            yline = RR[:,1]
            zline = RR[:,2]
            self.ax.plot3D(xline, yline, zline, 'white')
            self.ax.grid(False)
            self.ax.set_facecolor('black')

            img = plt.imread('clecio.jpg')

            theta = np.linspace(0, np.pi, img.shape[0])
            phi = np.linspace(0, 2*np.pi, img.shape[1])

            count = 50
            theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
            phi_inds = np.linspace(0, img.shape[1] - 1, count).round().astype(int)
            theta = theta[theta_inds]
            phi = phi[phi_inds]
            img = img[np.ix_(theta_inds, phi_inds)]

            theta,phi = np.meshgrid(theta, phi)

            
            x = 6353 * np.sin(theta) * np.cos(phi)
            y = 6353 * np.sin(theta) * np.sin(phi)
            z = 6353 * np.cos(theta)
            
            
            self.ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1) # we've already pruned ourselves
            RR=np.array(RR)
            robson=np.max(RR)
            self.ax.set_xlim(-robson,robson)
            self.ax.set_ylim(-robson,robson)
            self.ax.set_zlim(-robson,robson)
            '''
            phii = np.linspace(0,2*np.pi, 256).reshape(256, 1) # the angle of the projection in the xy-plane
            thetaa = np.linspace(0, np.pi, 256).reshape(-1, 256) # the angle from the polar axis, ie the polar angle
            radius = 6353

            # Transformation formulae for a spherical coordinate system.
            x = radius*np.sin(thetaa)*np.cos(phii)
            y = radius*np.sin(thetaa)*np.sin(phii)
            z = radius*np.cos(thetaa)
            self.ax.plot_surface(x, y, z, color='b')
            '''

            
        self.fig_canvas.draw()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())