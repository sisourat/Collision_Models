import matplotlib.pyplot as plt
import numpy as np

def model_cross_sections(labels,values):
    for label in labels:
        print(label,values[label])

    labels = ('Target Ionization Energy (eV):', 'Target electron radius (Angstrom):',
              'Target  mass (amu):', 'Target electron velocity (au):',
              'Target polarizability (Bohr^3)', 'Projectile charge:', 'Projectile mass (amu):')

    t_ie = float(values[labels[0]])/27.211
    t_r = float(values[labels[1]])
    t_m = float(values[labels[2]])*1818.2
    t_v = float(values[labels[3]])
    t_pol = float(values[labels[4]])
    p_q = float(values[labels[5]])
    p_m = float(values[labels[6]])*1818.2

    mu = t_m*p_m/(t_m+p_m)

    ecoll = np.arange(1e-4, 1e6, 0.1)  # start,stop,step
    vcoll = np.sqrt(ecoll/25000.0)
    langevin = 0.28*2.0*np.pi*p_q*np.sqrt(t_pol/mu)/vcoll
    cob = [0.28*np.pi*((1.0+2.0*np.sqrt(p_q))/t_ie)**2]*len(ecoll)
    lindhard = 0.28*8.0*np.pi*p_q**3/(t_v*t_r*vcoll**7)

    plt.xscale('log')
    plt.yscale('log')
    plt.ylim(0.0001, 10000.00)
    plt.xlabel('E (eV/amu)')
    plt.ylabel('Cross Sections (10$^-16$ cm$^2$)')
    plt.plot(ecoll, langevin, ecoll, cob, ecoll, lindhard)
    plt.legend(['Langevin', 'COB', 'Bohr-Lindhard'])
    plt.show()

