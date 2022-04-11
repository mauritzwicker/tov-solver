
def main_messy():
    const = Constants()

    defa = DefaultInput(const)

    # ** create user object
    usr_unchecked = UserInput(const)


    # * check user object
    usr = check_userinput(const, defa, usr_unchecked)


    ######################################################################
    ############################## ANALYSIS ##############################
    ######################################################################
    '''
    Plan:
    ** and need to determine phi
    - look at what factors we can change -> for each of these with different values get the data points for the following plots below
    - determine optimal gridsize, parameters values, and stuff for nice results
    -> save them so we can create the plots again without running sim again
    ->
    '''

    # What factors we can change:
    '''
        # self.K = 1.982e-6
        # self.gamma = 2.75

        # self.rho_c = 5.0e14 # g cm-3
        # self.p_c = None
        # self.eps_c = None
        # self.phi_c = None

        # self.m_c = 0

        # self.m_break = 1.5 * self.const.M_sun # g

        # self.r0 = 1e-8
    '''
    # FINAL PLOTS
    if False:
        print()
        '''
        THIS IS WHERE I AM SAVING MY FINAL PLOTS
        '''

        # PLOT (z_Rstar-rhoc_manyMstar)
        if False:
            # fixed: Mstar for each

            # In KM
            dep_varMAIN = const.M_sun * np.linspace(0.5, 2.5, 10)
            for varMAIN in dep_varMAIN:
                # Want: Rstar as function of rho_c
                dep_var = np.linspace(const.rho_nuc, const.rho_nuc*20, 20)
                vals_x = []
                vals_y = []
                for var in dep_var:
                    usr_unchecked1 = UserInput(const)
                    usr_unchecked1.m_break = varMAIN
                    usr_unchecked1.rho_c = var

                    usr1 = check_userinput(const, defa, usr_unchecked1)
                    tov1 = fcts.TOVmodel(usr1, const)
                    fcts.rk1(usr1, const, tov1)

                    if tov1.Mstar <= 100:
                        print('Mstar not reached!!')
                        continue


                    vals_x.append(var)
                    vals_y.append(tov1.Rstar)

                # in R_sun
                plt.plot(np.divide(vals_x,const.rho_nuc), const.R_sun_km * np.divide(vals_y,const.R_sun), label='{0}'.format(round(varMAIN/const.M_sun, 3)))
            plt.xlabel(r'$\rho_c$'' [nuclear-density]')
            plt.ylabel('R_star [km]')
            plt.xlim(0.5, 20)
            plt.legend(title='M_star [Msun]', loc='center left', bbox_to_anchor=(1, 0.5))
            plt.title('Star-Radius as function of Central-Density\nfor fixed Star-Mass'.format(round(defa.m_break/const.M_sun, 3)))
            plt.show()

            # # In km
            # plt.scatter(np.divide(vals_x,const.rho_nuc), const.R_sun_km * np.divide(vals_y,const.R_sun))
            # plt.xlabel('rho_c [nuclear-density]')
            # plt.ylabel('R_star [km]')
            # plt.title('Star-Radius as function of Central-Density\nfor fixed Star-Mass = {0} M_sun'.format(round(defa.m_break/const.M_sun, 3)))

        # PLOT (z_Rstar-rhoc_1o5Mstar)
        if False:
            # fixed: Mstar
            # Want: Rstar as function of rho_c
            dep_var = np.linspace(const.rho_nuc, const.rho_nuc*20, 50)
            vals_x = []
            vals_y = []
            break_ind = []
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.rho_c = var

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                if tov1.Mstar <= 100:
                    print('Mstar not reached!!')
                    continue

                break_ind.append(tov1.Mstarind)
                vals_x.append(var)
                vals_y.append(tov1.Rstar)

            # # in R_sun
            # plt.scatter(np.divide(vals_x,const.rho_nuc), np.divide(vals_y,const.R_sun), s=0)
            # plt.xlabel('rho_c [nuclear-density]')
            # plt.ylabel('R_star [R_sun]')
            # plt.title('Star-Radius as function of Central-Density\nfor fixed Star-Mass = {0} M_sun'.format(round(defa.m_break/const.M_sun, 3)))
            # plt.show()

            # In km
            plt.scatter(np.divide(vals_x,const.rho_nuc), const.R_sun_km * np.divide(vals_y,const.R_sun), color='darkblue', alpha=0.8)
            # plt.plot(np.divide(vals_x,const.rho_nuc), const.R_sun_km * np.divide(vals_y,const.R_sun), color='lightblue', alpha=0.7)
            plt.xlabel(r'$\rho_c$'' [nuclear-density]')
            plt.ylabel('R_star [km]')
            plt.title('Star-Radius as function of Central-Density\nfor fixed Star-Mass = {0} M_sun'.format(round(defa.m_break/const.M_sun, 3)))
            plt.show()

        # PLOT (z_Rstar-gridsize)
        if False:
            # How does gridsize affect results

            # after running these were the results
            stepsizes = [0.1, 0.14873521072935114, 0.2212216291070449, 0.32903445623126687, 0.4893900918477494, 0.7278953843983151, 1.0826367338740546, 1.6102620275609392, 2.395026619987486, 3.562247890262444, 5.29831690628371, 7.880462815669913, 11.721022975334806, 17.43328822199989, 25.92943797404667, 38.56620421163472, 57.361525104486816, 85.31678524172814, 126.89610031679234, 188.73918221350976, 280.72162039411785, 417.53189365604044, 621.0169418915616, 923.6708571873866, 1373.8237958832638, 2043.3597178569437, 3039.195382313201, 4520.35365636025, 6723.357536499335, 10000.0]
            models = [1395888.9859249063, 1395888.9745487077, 1395888.8893115227, 1395888.46719526, 1395888.3013471863, 1395887.8771967927, 1395886.8491168546, 1395886.2467951647, 1395883.8051472814, 1395881.1098915874, 1395878.70548934, 1395874.2894710193, 1395868.379075042, 1395848.5542536112, 1395833.5385689288, 1395826.663022547, 1395778.024653613, 1395697.3242528988, 1395603.345899226, 1395537.54799029, 1395467.209741575, 1394974.0914956685, 1394804.0863024096, 1393819.3583035353, 1393057.3638267238, 1391528.0026317637, 1391951.5198867943, 1387748.607188647, 1385011.6871390152, 1380000.034496561]
            del stepsizes[-4]
            del models[-4]
            print(stepsizes)
            print(models)
            plt.scatter(stepsizes, const.R_sun_km * np.divide(models, const.R_sun), color='darkblue', s=5)
            plt.title('Star-Radius as function of Simulation-Stepsize')
            plt.xlabel('Stepsize [cm]')
            plt.ylabel('R_star [km]')
            plt.xscale('log')
            plt.show()

            quit()

            # How Stepsize affects results
            dep_var = np.logspace(-1, 4, 30)
            models = []
            stepsizes = []
            # stepsize := the stepsize in the grid
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.stepsize = var
                usr_unchecked1.grid = int(4e7)

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                # models.append(tov1)
                if tov1.Mstar <= 0:
                    print('MSTAR NOT REACHED!!!')

                print('----------')
                print(var)
                print(tov1.r[0])
                print(tov1.r[1])
                print(tov1.Rstar)
                print('----------')
                stepsizes.append(var)
                models.append(tov1.Rstar)

            print(stepsizes)
            print(models)
            plt.scatter(stepsizes, const.R_sun_km * np.divide(models, const.R_sun), color='darkblue', s=1.4)
            plt.xlabel('Stepsize [cm]')
            plt.ylabel('R_star [km]')
            plt.xscale('log')
            plt.show()







    # usr_unchecked1 = UserInput(const)
    # usr_unchecked1.r_type = 'lin'
    # usr1 = check_userinput(const, defa, usr_unchecked1)
    # tov1 = fcts.TOVmodel(usr1, const)
    # fcts.rk1(usr, const, tov1)


    ############ THESE ARE ALL GOOD ADD TO ABOVE ############

    # THESE TWO ARE GOOD -> JUST FINISH
    # -- z_GOOD-ONE.png --
    if False:
        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 1.5 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc

        # so if rho_c is lower -> we need more iterations -> radius is bigger

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk1(usr1, const, tov1)

        if tov1.Pzero == True:
            print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
            print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
            print('You set M_brak = {0}'.format(usr.m_break/const.M_sun))
        elif tov1.Pzero == False:
            print('M-BREAK REACHED')

        if True:
            gs = gridspec.GridSpec(2, 2)

            fig = plt.figure()
            ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
            ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
            ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

            ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
            ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
            ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc))
            ax1.set_xscale('log')
            ax1.set_xlim(1e-1, 2e1)
            ax2.set_xlim(1e-1, 2e1)
            ax3.set_xlim(1e-1, 2e1)
            ax2.set_xscale('log')
            ax3.set_xscale('log')
            # ax3.legend(title='M_star', loc='center left', bbox_to_anchor=(1, 0.5))
            ax1.set_title('Mass of Object\nas function of Radius')
            ax2.set_title('Pressure of Object\nas function of Radius')
            ax3.set_title('Density of Object\nas function of Radius')
            fig.tight_layout()
            plt.show()

        quit()

    # Now same as above but find where m_break is (ie p-> zero) for different rho_c
    # we see that after a specific rho_c (between 2-2.66) the rstar begins to decrease
    # -- z_rhoc_maxAll.png --
    if False:
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns


        rho_cvals = np.linspace(1, 4, 10)
        rho_cvals = np.linspace(2.2, 2.3, 10)
        for vari in rho_cvals:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.m_break = 10 * const.M_sun
            usr_unchecked1.rho_c = vari * const.rho_nuc

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            print()
            print(vari)
            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')



            ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
            ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
            ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='{0}'.format(str(round(vari, 3))))
        ax1.set_xscale('log')
        ax1.set_xlim(1e-1, 2e1)
        ax2.set_xlim(1e-1, 2e1)
        ax3.set_xlim(1e-1, 2e1)
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        ax3.legend(title='rho_c', loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_title('Mass of Object\nas function of Radius')
        ax2.set_title('Pressure of Object\nas function of Radius')
        ax3.set_title('Density of Object\nas function of Radius')
        fig.tight_layout()
        plt.show()

    # -- z_rho_vs_MR.png --
    # Now we want a list of Mstar and Rstar for different central densities (ie when pressure = 0)
    if False:
        rho_cvals = np.linspace(1, 10, 100)
        rstar_vals = []
        mstar_vals = []
        for vari in rho_cvals:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.m_break = 100 * const.M_sun
            usr_unchecked1.rho_c = vari * const.rho_nuc

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            print()
            print(vari)
            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')
            rstar_vals.append(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun))
            mstar_vals.append(tov1.Mstar/const.M_sun)

        fig, ax = plt.subplots(2,1, sharex=True)
        ax[0].scatter(rho_cvals, rstar_vals)
        ax[1].scatter(rho_cvals, mstar_vals)
        plt.show()

    # -- z_gammkapp.png --
    # Now for one good parameter -> find how Kappa and gamma affect it
    if False:
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        ###########################
        # GAMMA
        ###########################
        if False:
            gam_vals = np.linspace(2.7, 2.8, 10)
            rstar_vals = []
            mstar_vals = []
            for vari in gam_vals:
                usr_unchecked1 = UserInput(const)
                # usr_unchecked1.m_break = 10 * const.M_sun
                usr_unchecked1.gamma = vari

                # so if rho_c is lower -> we need more iterations -> radius is bigger

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                print()
                print(vari)
                if tov1.Pzero == True:
                    print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                    print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                    print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                    # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
                elif tov1.Pzero == False:
                    print('M-BREAK REACHED')

                rstar_vals.append(tov1.Rstar)
                mstar_vals.append(tov1.Mstar)



                ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
                ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
                ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='{0}'.format(str(round(vari, 3))))
            ax1.set_xscale('log')
            ax1.set_xlim(1e-1, 2e1)
            ax2.set_xlim(1e-1, 2e1)
            ax3.set_xlim(1e-1, 2e1)
            ax2.set_xscale('log')
            ax3.set_xscale('log')
            ax3.legend(title='gamma', loc='center left', bbox_to_anchor=(1, 0.5))
            ax1.set_title('Mass of Object\nas function of Radius')
            ax2.set_title('Pressure of Object\nas function of Radius')
            ax3.set_title('Density of Object\nas function of Radius')
            fig.tight_layout()
            plt.show()

            # Print gamma vs rstar and mstar
            if True:
                fig, ax = plt.subplots(2,1, sharex=True)
                ax[0].scatter(gam_vals, rstar_vals)
                ax[1].scatter(gam_vals, mstar_vals)
                plt.show()

        ###########################
        # KAPPA
        ###########################
        if False:
            kap_vals = np.linspace(1e-6, 1e-5, 10)
            rstar_vals = []
            mstar_vals = []
            for vari in kap_vals:
                usr_unchecked1 = UserInput(const)
                # usr_unchecked1.m_break = 10 * const.M_sun
                usr_unchecked1.K = vari

                # so if rho_c is lower -> we need more iterations -> radius is bigger

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                print()
                print(vari)
                if tov1.Pzero == True:
                    print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                    print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                    print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                    # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
                elif tov1.Pzero == False:
                    print('M-BREAK REACHED')

                rstar_vals.append(tov1.Rstar)
                mstar_vals.append(tov1.Mstar)



                ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
                ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
                ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='{0}'.format(str(round(vari, 3))))
            ax1.set_xscale('log')
            ax1.set_xlim(1e-1, 2e1)
            ax2.set_xlim(1e-1, 2e1)
            ax3.set_xlim(1e-1, 2e1)
            ax2.set_xscale('log')
            ax3.set_xscale('log')
            ax3.legend(title='Kappa', loc='center left', bbox_to_anchor=(1, 0.5))
            ax1.set_title('Mass of Object\nas function of Radius')
            ax2.set_title('Pressure of Object\nas function of Radius')
            ax3.set_title('Density of Object\nas function of Radius')
            fig.tight_layout()
            plt.show()

            # Print gamma vs rstar and mstar
            if True:
                fig, ax = plt.subplots(2,1, sharex=True)
                ax[0].scatter(kap_vals, rstar_vals)
                ax[1].scatter(kap_vals, mstar_vals)
                plt.show()

    # -- z_rkmethods.png --
    if False:
        tovs = []
        for rksel in [1,2,3,4]:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.m_break = 2 * const.M_sun
            usr_unchecked1.rho_c = 1.9 * const.rho_nuc
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)

            if rksel == 1:
                fcts.rk1(usr1, const, tov1)
            elif rksel == 2:
                fcts.rk2(usr1, const, tov1)
            elif rksel == 3:
                fcts.rk3(usr1, const, tov1)
            elif rksel == 4:
                fcts.rk4(usr1, const, tov1)

            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

            tovs.append(tov1)

        for rksel, tovi in enumerate(tovs):
            print('RK-{0}'.format(str(rksel+1)))
            print(tovi.Rstar*const.R_sun_km/const.R_sun)
            print(tovi.Mstar/const.M_sun)
            print()

        if False:
            for rksel, tovi in enumerate(tovs):
                plt.plot(const.R_sun_km*np.divide(tovi.r[:tovi.Mstarind],const.R_sun), np.divide(tovi.m[:tovi.Mstarind], const.M_sun), label='RK-{0}'.format(str(rksel+1)), linewidth=0.6)
            plt.xscale('log')
            plt.xlim(5e0, 2e1)
            plt.legend()
            plt.show()

        # PLot difference of RK4 to rest
        if False:
            for rksel, tovi in enumerate(tovs):
                # if rksel == 3:
                #     continue
                xfin = const.R_sun_km*np.divide(tovi.r[:tovi.Mstarind],const.R_sun)
                y = np.divide(tovi.m[:tovi.Mstarind], const.M_sun)
                # x4 = const.R_sun_km*np.divide(tovs[-1].r[:tovs[-1].Mstarind],const.R_sun)
                # x4 = x4[:len(x)]
                # xfin = np.subtract(x, x4)
                y4 = np.divide(tovs[-1].m[:tovs[-1].Mstarind], const.M_sun)
                y4 = y4[:len(y)]
                yfin = np.subtract(y, y4)

                plt.plot(xfin, yfin, label='RK-{0}'.format(str(rksel+1)))
            # plt.xscale('log')
            # plt.xlim(5e0, 2e1)
            plt.legend()
            plt.show()

        quit()
    # why is 2 the same as 4? -> it is not just very similar
    if False:
        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 2 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc
        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)

        fcts.rk2(usr1, const, tov1)

        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 2 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc
        usr2 = check_userinput(const, defa, usr_unchecked1)
        tov2 = fcts.TOVmodel(usr1, const)

        fcts.rk4(usr2, const, tov2)

        print(tov1.m[0:10])
        print(tov2.m[0:10])
        print(tov1.Mstar)
        print(tov2.Mstar)
        print(tov1.Rstar)
        print(tov2.Rstar)
        plt.scatter(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label='rk2')
        plt.scatter(tov2.r[:tov2.Mstarind], tov2.m[:tov2.Mstarind], label='rk4')
        plt.show()
        plt.scatter(tov1.r[:tov1.Mstarind], np.subtract(tov1.m[:tov1.Mstarind], tov2.m[:tov1.Mstarind]))
        plt.show()
        quit()


    # try schwarzschild thing
    if False:
        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 1.5 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc

        # so if rho_c is lower -> we need more iterations -> radius is bigger

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk1(usr1, const, tov1)

        if tov1.Pzero == True:
            print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
            print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
            print('You set M_brak = {0}'.format(usr.m_break/const.M_sun))
        elif tov1.Pzero == False:
            print('M-BREAK REACHED')


        # DETERMINE PHI
        phi_r = np.zeros(tov1.Mstarind)
        phi_r[-1] = 0.5 * np.log(1 - (2*const.G*tov1.m[:tov1.Mstarind][-1]/(tov1.r[:tov1.Mstarind][-1] * (const.c**2))))

        for i in range(len(phi_r)-2, -1, -1):

            dphi_dr = (tov1.m[i] + (4*np.pi*(tov1.r[i]**3)*tov1.p[i]/(const.c**2))) / (tov1.r[i] * (tov1.r[i] - (2 * const.G * tov1.m[i] / (const.c**2))))
            phi_r[i] = phi_r[i+1] + dphi_dr

        print(phi_r)
        plt.scatter(tov1.r[:tov1.Mstarind], phi_r)
        plt.show()

        ### IS IT + or - ?????

        quit()



    # try post netownian correction!
    if False:
        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 4 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc

        # so if rho_c is lower -> we need more iterations -> radius is bigger
        # --- Newtonian ---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1_newtonian(usr1, const, tov1)

            if tov1.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('You set M_break = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

        # --- NORMAL ---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov2 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov2)

            if tov2.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov2.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov2.Pzero == False:
                print('M-BREAK REACHED')


        plt.plot(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label='NEW')
        plt.plot(tov2.r[:tov2.Mstarind], tov2.m[:tov2.Mstarind], label='GR')
        plt.legend()
        plt.show()



    # also try including epsilon
    if False:
        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 4 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc

        # --- NORMAL WITHOUT EPSILON---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            if tov1.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

        # --- NORMAL WITH EPSILON---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov2 = fcts.TOVmodel(usr1, const)
            fcts.rk1_incl_epsilon(usr1, const, tov2)

            if tov2.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov2.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov2.Pzero == False:
                print('M-BREAK REACHED')

        plt.scatter(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label='normal')
        plt.scatter(tov2.r[:tov2.Mstarind], tov2.m[:tov2.Mstarind], label='with eps')
        plt.legend()
        plt.show()

    ############ THESE ARE ALL GOOD ADD TO ABOVE ############


    # compare times for rk
    if False:
        rk1s = []
        rk2s = []
        rk3s = []
        rk4s = []
        for j in range(0, 100):
            print('\n********')
            print(j)
            print('********\n')
            for i in range(1,5):
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.m_break = 3 * const.M_sun
                usr_unchecked1.rho_c = 1.9 * const.rho_nuc

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)

                t1 = 0
                t2 = 0

                if i == 1:
                    t1 = time.perf_counter()
                    fcts.rk1(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk1s.append(t2-t1)

                elif i == 2:
                    t1 = time.perf_counter()
                    fcts.rk2(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk2s.append(t2-t1)

                elif i == 3:
                    t1 = time.perf_counter()
                    fcts.rk3(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk3s.append(t2-t1)

                elif i == 4:
                    t1 = time.perf_counter()
                    fcts.rk4(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk4s.append(t2-t1)

        # now we can get an average
        plt.hist(rk1s, label='rk1')
        plt.hist(rk2s, label='rk2')
        plt.hist(rk3s, label='rk3')
        plt.hist(rk4s, label='rk4')
        plt.legend()
        plt.show()




    ##### PLOTS IN PAPER:
    # Section 1: A Representative Model
    if False:
        usr_unchecked1 = UserInput(const)
        # so if rho_c is lower -> we need more iterations -> radius is bigger

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk4(usr1, const, tov1)

        ### print Parameters
        print()
        print(usr1.rho_c)
        print(usr1.K)
        print(usr1.gamma)
        print()
        ###

        if tov1.Pzero == True:
            print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
            print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
            print('You set M_brak = {0}'.format(usr.m_break/const.M_sun))
        elif tov1.Pzero == False:
            print('M-BREAK REACHED')

        ### print results
        print()
        print('Found Results at marker: {0}'.format(tov1.Mstarind))
        print('{0} g'.format(tov1.Mstar))
        print('{0} Msun'.format(tov1.Mstar/const.M_sun))
        print('{0} cm'.format(tov1.Rstar))
        print('{0} Rsun'.format(const.R_sun_km * tov1.Rstar / const.R_sun))
        print()
        ###

        ### Plots
        # m(r)
        plt.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun), color='darkblue')
        plt.xlabel('r  [km]')
        plt.xscale('log')
        plt.xlim(1e-1, 2e1)
        plt.ylabel('Mass  [' r'$M_{\odot}$' ']')
        plt.show()
        # p(r)
        plt.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind], color='darkblue')
        plt.xlabel('r  [km]')
        plt.xscale('log')
        plt.xlim(1e-1, 2e1)
        plt.ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
        plt.show()
        # rho(r)
        plt.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), color='darkblue')
        plt.xlabel('r  [km]')
        plt.xscale('log')
        plt.xlim(1e-1, 2e1)
        plt.ylabel('Density  [' r'$\rho_{nuc}$' ']')
        plt.show()
        ###
        quit()

        if True:
            gs = gridspec.GridSpec(2, 2)

            fig = plt.figure()
            ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
            ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
            ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

            ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
            ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
            ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc))
            ax1.set_xscale('log')
            ax1.set_xlim(1e-1, 2e1)
            ax2.set_xlim(1e-1, 2e1)
            ax3.set_xlim(1e-1, 2e1)
            ax2.set_xscale('log')
            ax3.set_xscale('log')
            # ax3.legend(title='M_star', loc='center left', bbox_to_anchor=(1, 0.5))
            ax1.set_title('Mass of Object\nas function of Radius')
            ax2.set_title('Pressure of Object\nas function of Radius')
            ax3.set_title('Density of Object\nas function of Radius')
            fig.tight_layout()
            plt.show()

    # Section 2: Radius-Mass Relation
    if False:
        rho_cvals = np.linspace(1, 30, 100)
        rstar_vals = []
        mstar_vals = []
        for vari in rho_cvals:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.m_break = 100 * const.M_sun
            usr_unchecked1.rho_c = vari * const.rho_nuc

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            print()
            print(vari)
            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

            rstar_vals.append(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun))
            mstar_vals.append(tov1.Mstar/const.M_sun)

        ### PLOTS
        # R(M)
        plt.scatter(mstar_vals, rstar_vals, color='darkblue', marker='.', s=30)
        plt.xlabel('Star-Mass  [' r'$M_{\odot}$' ']')
        plt.ylabel('Star-Radius  [km]')
        plt.show()
        plt.scatter(rstar_vals, mstar_vals, color='darkblue', marker='.', s=30)
        plt.xlabel('Star-Mass  [' r'$M_{\odot}$' ']')
        plt.ylabel('Star-Radius  [km]')
        plt.show()
        # M(rho_c)
        plt.scatter(rho_cvals, mstar_vals, color='darkblue', marker='.', s=30)
        plt.xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        plt.ylabel('Star-Mass  [' r'$M_{\odot}$' ']')
        plt.show()
        # R(rho_c)
        plt.scatter(rho_cvals, rstar_vals, color='darkblue', marker='.', s=30)
        plt.xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        plt.ylabel('Star-Radius  [km]')
        plt.show()

        # sunplots M(rho_c) and R(rho_c)
        fig, ax = plt.subplots(1,2, sharex=True)
        ax[0].scatter(rho_cvals, mstar_vals, color='darkblue', marker='.', s=30)
        ax[0].set_xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        ax[0].set_ylabel('Star-Mass  [' r'$M_{\odot}$' ']')
        # R(rho_c)
        ax[1].scatter(rho_cvals, rstar_vals, color='darkblue', marker='.', s=30)
        ax[1].set_xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        ax[1].set_ylabel('Star-Radius  [km]')
        plt.show()

        ###
        # fig, ax = plt.subplots(2,1, sharex=True)
        # ax[0].scatter(rho_cvals, rstar_vals)
        # ax[1].scatter(rho_cvals, mstar_vals)
        # plt.show()
    # To find Maximum radius
    if False:
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1], sharex=ax1) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        rho_cvals = np.linspace(2.2, 2.35, 10)
        rstars = []
        for aa, vari in enumerate(rho_cvals):
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.rho_c = vari * const.rho_nuc

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            # print()
            # print(vari)
            # if tov1.Pzero == True:
            #     print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
            #     print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
            #     print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
            #     # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
            # elif tov1.Pzero == False:
            #     print('M-BREAK REACHED')
            print('rhoc-val = {0}'.format(vari))
            print('Rstar = {0}'.format(tov1.Rstar))
            print('Ind = {0}'.format(tov1.Mstarind))
            rstars.append(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun))

            ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
            ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
            ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='{0}'.format(str(round(vari, 3))))
        ax1.set_xscale('log')
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        # ax1.set_xlabel('r  [km]')
        # ax2.set_xlabel('r  [km]')
        ax1.set_xlim(1.4295e1, 1.435e1)
        ax2.set_xlim(1.4295e1, 1.435e1)
        ax3.set_xlim(1.4295e1, 1.435e1)
        ax1.set_ylim(1.80, 2.0)
        ax2.set_ylim(-0.1e31, 1.5e31)
        ax3.set_ylim(0.0, 0.1)
        # ax3.set_xlabel('r  [km]')
        ax3.legend(title='rho_c [' r'$\rho_{nuc}$' ']', loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_ylabel('Mass  [' r'$M_{\odot}$' ']')
        ax2.set_ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
        ax3.set_ylabel('Density  [' r'$\rho_{nuc}$' ']')
        ax1.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)
        ax2.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)
        ax3.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)
        # fig.tight_layout()
        plt.show()

        # When we plot the
        plt.scatter(rho_cvals, rstars, color='darkblue')
        plt.xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        plt.ylabel('Star-Radius  [km]')
        plt.show()
    # To find more exactly
    if False:
        rho_cvals = np.linspace(2.25, 2.32, 10)
        rstars = []
        for aa, vari in enumerate(rho_cvals):
            if vari >= 2.29:
                continue
            if vari <= 2.285:
                continue
            print('\n\n\n')
            print(vari)
            print('\n\n\n')

            usr_unchecked1 = UserInput(const)
            usr_unchecked1.rho_c = vari * const.rho_nuc
            usr_unchecked1.stepsize = 1

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk4(usr1, const, tov1)

            print('rhoc-val = {0}'.format(vari))
            print('Rstar = {0}'.format(tov1.Rstar))
            print('Ind = {0}'.format(tov1.Mstarind))
            print('Mstar = {0}'.format(tov1.Mstar/const.M_sun))
            quit()
            rstars.append(tov1.Rstar *1e-5)



        # When we plot the
        plt.scatter(rho_cvals, rstars, color='darkblue')
        plt.xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        plt.ylabel('Star-Radius  [km]')
        plt.show()

        for i,j in zip(rho_cvals, rstars):
            print('{0} -- {1}'.format(i,j))
    # To find Maximum Mass
    if False:
        rho_cvals = np.linspace(6.4, 6.48, 10)
        mstars = []
        for aa, vari in enumerate(rho_cvals):
            print(aa)
            if vari <= 6.435:
                continue
            if vari >= 6.436:
                continue
            print('\n\n\n')
            print(vari)
            print('\n\n\n')

            usr_unchecked1 = UserInput(const)
            usr_unchecked1.rho_c = vari * const.rho_nuc
            usr_unchecked1.stepsize = 1

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            print('rhoc-val = {0}'.format(vari))
            print('Rstar = {0}'.format(tov1.Rstar))
            print('Ind = {0}'.format(tov1.Mstarind))
            print('Mstar = {0}'.format(tov1.Mstar/const.M_sun))
            print('Rstar = {0}'.format(tov1.Rstar*1e-5))
            print('here')
            quit()

            mstars.append(tov1.Mstar/const.M_sun)


        for i,j in zip(rho_cvals, mstars):
            print('{0} -- {1}'.format(i,j))

        # When we plot the
        plt.scatter(rho_cvals, mstars, color='darkblue')
        plt.xlabel('Central-Density  [' r'$\rho_{nuc}$' ']')
        plt.ylabel('Star-Mass  [' r'$M_{\odot}$' ']')
        plt.show()

    # Section 3: Numerical Parameters: Gridsize
    if False:
        # dep_var = np.logspace(0, 5, 6)
        dep_var1 = np.linspace(1, 10, 10)
        dep_var2 = np.linspace(20, 100, 9)
        dep_var3 = np.linspace(200, 1000, 9)
        dep_var4 = np.linspace(1100, 10000, 9)
        dep_var5 = np.linspace(11000, 100000, 9)
        dep_var6 = np.linspace(110000, 1000000, 9)
        dep_var = np.concatenate((dep_var1, dep_var2, dep_var3, dep_var4, dep_var5, dep_var6))
        dep_var = np.logspace(0, 6, 50)
        tovs = []
        mstars = []
        minds = []
        rstars = []
        for var in dep_var:
            print(var)
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.stepsize = var

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            tovs.append(tov1)
            mstars.append(tov1.Mstar/const.M_sun)
            minds.append(tov1.Mstarind)
            rstars.append(tov1.Rstar * 1e-5)

            print(tov1.Mstarind)

        print()
        print(dep_var)
        print(mstars)
        print(minds)
        print(rstars)
        print()

        fig, ax = plt.subplots(1,2, sharex=True)
        ax[0].scatter(dep_var, mstars, color='darkblue', marker='.', s=30)
        ax[0].set_xlabel('Stepsize [cm]')
        ax[0].set_xscale('log')
        ax[0].set_ylabel('Star-Mass  [' r'$M_{\odot}$' ']')

        ax[1].scatter(dep_var, rstars, color='darkblue', marker='.', s=30)
        ax[1].set_xlabel('Stepsize [cm]')
        ax[1].set_xscale('log')
        ax[1].set_ylabel('Star-Radius  [km]')
        plt.show()

        quit()
    # Then for 1, 10000 to plot m(r) and stuff
    if False:
        dep_var = np.logspace(0, 6, 7)
        tovs = []
        mstars = []
        minds = []
        rstars = []
        for var in dep_var:
            print(var)
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.stepsize = var

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            tovs.append(tov1)
            mstars.append(tov1.Mstar)
            minds.append(tov1.Mstarind)
            rstars.append(tov1.Rstar)

        if True:
            gs = gridspec.GridSpec(2, 2)

            fig = plt.figure()
            ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
            ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
            ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns
            for aa, tov1 in zip(dep_var, tovs):
                ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
                ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
                ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label=str(aa))
            ax3.set_xlabel('r  [km]')
            ax1.set_ylabel('Mass  [' r'$M_{\odot}$' ']')
            ax2.set_ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
            ax3.set_ylabel('Density  [' r'$\rho_{nuc}$' ']')
            ax1.set_xscale('log')
            ax1.set_xlim(1e0, 3e1)
            ax2.set_xlim(1e0, 3e1)
            ax3.set_xlim(1e0, 3e1)
            ax2.set_xscale('log')
            ax3.set_xscale('log')
            ax3.legend(title='Stepsize [cm]', loc='center left', bbox_to_anchor=(1, 0.5))
            fig.tight_layout()
            plt.show()

    # Section 4: Numerical Parameters: Runge-Kutta Order
    if False:
        tovs = []
        for rksel in [1,2,3,4]:
            usr_unchecked1 = UserInput(const)
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)

            if rksel == 1:
                fcts.rk1(usr1, const, tov1)
            elif rksel == 2:
                fcts.rk2(usr1, const, tov1)
            elif rksel == 3:
                fcts.rk3(usr1, const, tov1)
            elif rksel == 4:
                fcts.rk4(usr1, const, tov1)

            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

            tovs.append(tov1)

        for rksel, tovi in enumerate(tovs):
            print('RK-{0}'.format(str(rksel+1)))
            print(tovi.Rstar*const.R_sun_km/const.R_sun)
            print(tovi.Mstar/const.M_sun)
            print()

        if False:
            for rksel, tovi in enumerate(tovs):
                plt.plot(const.R_sun_km*np.divide(tovi.r[:tovi.Mstarind],const.R_sun), np.divide(tovi.m[:tovi.Mstarind], const.M_sun), label='RK-{0}'.format(str(rksel+1)), linewidth=0.6)
            plt.xscale('log')
            plt.xlim(5e0, 2e1)
            plt.legend()
            plt.show()

        # PLot difference of RK4 to rest
        if False:
            for rksel, tovi in enumerate(tovs):
                if rksel == 3:
                    continue
                xfin = const.R_sun_km*np.divide(tovi.r[:tovi.Mstarind],const.R_sun)
                y = np.divide(tovi.m[:tovi.Mstarind], const.M_sun)
                # x4 = const.R_sun_km*np.divide(tovs[-1].r[:tovs[-1].Mstarind],const.R_sun)
                # x4 = x4[:len(x)]
                # xfin = np.subtract(x, x4)
                y4 = np.divide(tovs[-1].m[:tovs[-1].Mstarind], const.M_sun)
                y4 = y4[:len(y)]
                yfin = np.subtract(y, y4)
                plt.xlabel('r  [km]')
                plt.ylabel('Mass  [' r'$M_{\odot}$' ']')
                # plt.title('Deviation of Mass-Profile for RK method 1,2,3 from RK-4 method')
                plt.plot(xfin, yfin, label='RK-{0}'.format(str(rksel+1)))
            # plt.xscale('log')
            # plt.xlim(5e0, 2e1)
            plt.legend()
            plt.show()

            for rksel, tovi in enumerate(tovs):
                if rksel == 3:
                    continue
                xfin = const.R_sun_km*np.divide(tovi.r[:tovi.Mstarind],const.R_sun)
                y = np.divide(tovi.rho[:tovi.Mstarind], const.rho_nuc)
                # x4 = const.R_sun_km*np.divide(tovs[-1].r[:tovs[-1].Mstarind],const.R_sun)
                # x4 = x4[:len(x)]
                # xfin = np.subtract(x, x4)
                y4 = np.divide(tovs[-1].rho[:tovs[-1].Mstarind], const.rho_nuc)
                y4 = y4[:len(y)]
                yfin = np.subtract(y, y4)
                plt.xlabel('r  [km]')
                plt.ylabel('Density  [' r'$\rho_{nuc}$' ']')
                plt.title('Deviation of Mass-Profile for RK method 1,2,3 from RK-4 method')
                plt.plot(xfin, yfin, label='RK-{0}'.format(str(rksel+1)))

            plt.legend()
            plt.show()

            for rksel, tovi in enumerate(tovs):
                if rksel == 3:
                    continue
                xfin = const.R_sun_km*np.divide(tovi.r[:tovi.Mstarind],const.R_sun)
                y = tovi.p[:tovi.Mstarind]
                # x4 = const.R_sun_km*np.divide(tovs[-1].r[:tovs[-1].Mstarind],const.R_sun)
                # x4 = x4[:len(x)]
                # xfin = np.subtract(x, x4)
                y4 = tovs[-1].p[:tovs[-1].Mstarind]
                y4 = y4[:len(y)]
                yfin = np.subtract(y, y4)
                plt.xlabel('r  [km]')
                plt.ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
                plt.title('Deviation of Mass-Profile for RK method 1,2,3 from RK-4 method')
                plt.plot(xfin, yfin, label='RK-{0}'.format(str(rksel+1)))

            plt.legend()
            plt.show()

        quit()
    # compare times for rk
    if False:
        rk1s = []
        rk2s = []
        rk3s = []
        rk4s = []
        for j in range(0, 1000):
            print('\n********')
            print(j)
            print('********\n')
            for i in range(1,5):
                usr_unchecked1 = UserInput(const)

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)

                t1 = 0
                t2 = 0

                if i == 1:
                    t1 = time.perf_counter()
                    fcts.rk1(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk1s.append(t2-t1)

                elif i == 2:
                    t1 = time.perf_counter()
                    fcts.rk2(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk2s.append(t2-t1)

                elif i == 3:
                    t1 = time.perf_counter()
                    fcts.rk3(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk3s.append(t2-t1)

                elif i == 4:
                    t1 = time.perf_counter()
                    fcts.rk4(usr1, const, tov1)
                    t2 = time.perf_counter()
                    rk4s.append(t2-t1)

        # now we can get an average
        plt.hist(rk1s, label='rk1', bins=50, alpha=0.5)
        plt.hist(rk2s, label='rk2', bins=50, alpha=0.5)
        plt.hist(rk3s, label='rk3', bins=50, alpha=0.5)
        plt.hist(rk4s, label='rk4', bins=50, alpha=0.5)
        plt.xlabel('Run-time [s]')
        plt.legend()
        plt.show()

        # differences to RK 4
        print('')
        rk1s = np.divide(rk1s, np.median(rk4s))
        print('\nAverage RK1 to RK4')
        print(np.median(rk1s))
        print(np.std(rk1s))
        rk2s = np.divide(rk2s, np.median(rk4s))
        print('\nAverage RK2 to RK4')
        print(np.median(rk2s))
        print(np.std(rk2s))
        rk3s = np.divide(rk3s, np.median(rk4s))
        print('\nAverage RK3 to RK4')
        print(np.median(rk3s))
        print(np.std(rk3s))

    # Section 5: Polytropic EoS Parameters
    # gamma
    if False:
        # Gamma
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        ###########################
        # GAMMA
        ###########################
        gam_vals = np.linspace(2.7, 2.8, 10)
        gam_vals = np.linspace(2.5, 3.2, 100)
        # gam_vals = np.append(gam_vals, 2.75)
        rstar_vals = []
        mstar_vals = []
        for vari in gam_vals:
            usr_unchecked1 = UserInput(const)
            # usr_unchecked1.m_break = 10 * const.M_sun
            usr_unchecked1.gamma = vari

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            print()
            print(vari)
            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

            rstar_vals.append(tov1.Rstar)
            mstar_vals.append(tov1.Mstar)


            ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
            ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
            ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='{0}'.format(str(round(vari, 3))))
        ax1.set_xlim(1e-3, 2e3)
        ax2.set_xlim(1e-3, 2e3)
        ax3.set_xlim(1e-3, 2e3)
        ax1.set_xscale('log')
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        ax3.legend(title='gamma', loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_title('Mass of Object\nas function of Radius')
        ax2.set_title('Pressure of Object\nas function of Radius')
        ax3.set_title('Density of Object\nas function of Radius')
        ax3.set_xlabel('r  [km]')
        ax1.set_ylabel('Mass  [' r'$M_{\odot}$' ']')
        ax2.set_ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
        ax3.set_ylabel('Density  [' r'$\rho_{nuc}$' ']')
        fig.tight_layout()
        plt.show()


        usr_unchecked1 = UserInput(const)
        usr_unchecked1.gamma = 2.75

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk1(usr1, const, tov1)
        mval275 = tov1.Mstar
        rval275 = tov1.Rstar

        # Print gamma vs rstar and mstar
        if True:
            fig, ax = plt.subplots(1,2, sharex=True)
            ax[0].scatter(gam_vals, np.multiply(1e-5, rstar_vals), color='darkblue', s=30)
            ax[0].scatter(2.75, np.multiply(1e-5, rval275), color='orange', label=r'$\gamma$' ' = 2.75', s=30)
            ax[0].set_xlabel(r'$\gamma$')
            ax[0].set_ylabel('Star-Radius  [km]')
            ax[1].scatter(gam_vals, np.divide(mstar_vals, const.M_sun), color='darkblue', s=30)
            ax[1].scatter(2.75, np.divide(mval275, const.M_sun), color='orange', label=r'$\gamma$' ' = 2.75', s=30)
            ax[1].set_xlabel(r'$\gamma$')
            ax[1].set_ylabel('Star-Mass  [' r'$M_{\odot}$' ']')
            ax[0].legend()
            ax[1].legend()
            plt.show()
    # K
    if False:
        ###########################
        # KAPPA
        ###########################
        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        kap_vals = np.linspace(1e-7, 1e-1, 10)
        kap_vals = np.logspace(-7, 0, 100)
        rstar_vals = []
        mstar_vals = []
        for vari in kap_vals:
            usr_unchecked1 = UserInput(const)
            # usr_unchecked1.m_break = 10 * const.M_sun
            usr_unchecked1.K = vari

            # so if rho_c is lower -> we need more iterations -> radius is bigger

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            print()
            print(vari)
            if tov1.Pzero == True:
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('R-star = {0} Rearth'.format(const.R_sun_km * np.divide(tov1.Rstar, const.R_sun)))
                # print('You set M_break = {0}'.format(usr.m_break/const.M_sun))
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

            rstar_vals.append(tov1.Rstar)
            mstar_vals.append(tov1.Mstar)

            ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun))
            ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind])
            ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='{0:3e}'.format(vari))
        ax1.set_xscale('log')
        ax1.set_xlim(1e-1, 2e2)
        ax2.set_xlim(1e-1, 2e2)
        ax3.set_xlim(1e-1, 2e2)
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        ax3.legend(title='Kappa', loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_title('Mass of Object\nas function of Radius')
        ax2.set_title('Pressure of Object\nas function of Radius')
        ax3.set_title('Density of Object\nas function of Radius')
        fig.tight_layout()
        plt.show()


        usr_unchecked1 = UserInput(const)
        usr_unchecked1.K = 1.982e-6

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk1(usr1, const, tov1)
        mval275 = tov1.Mstar
        rval275 = tov1.Rstar


        # Print gamma vs rstar and mstar
        if True:
            fig, ax = plt.subplots(1,2, sharex=True)
            ax[0].scatter(kap_vals, np.multiply(1e-5, rstar_vals), color='darkblue', s=30)
            ax[0].scatter(1.982e-6, np.multiply(1e-5, rval275), color='orange', label='K = 1.982e-6', s=30)
            ax[0].set_xlabel('K')
            ax[0].set_ylabel('Star-Radius  [km]')
            ax[1].scatter(kap_vals, np.divide(mstar_vals, const.M_sun), color='darkblue', s=30)
            ax[1].scatter(1.982e-6, np.divide(mval275, const.M_sun), color='orange', label='K = 1.982e-6', s=30)
            ax[1].set_xlabel('K')
            ax[1].set_ylabel('Star-Mass  [' r'$M_{\odot}$' ']')
            ax[0].legend()
            ax[0].set_xscale('log')
            ax[1].set_xscale('log')
            ax[1].legend()
            plt.show()

    # ?????
    # Section 6: Metric Potential
    if False:
        usr_unchecked1 = UserInput(const)

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk1(usr1, const, tov1)

        if tov1.Pzero == True:
            print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
            print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
            print('You set M_brak = {0}'.format(usr.m_break/const.M_sun))
        elif tov1.Pzero == False:
            print('M-BREAK REACHED')


        # DETERMINE PHI
        phi_r = np.zeros(tov1.Mstarind)
        # phi_r[-1] = 0.5 * np.log(1 - (2*const.G*tov1.m[:tov1.Mstarind][-1]/(tov1.r[:tov1.Mstarind][-1] * (const.c**2))))
        phi_r[-1] = 0.5 * np.log(1 - (2*const.G*tov1.m[:tov1.Mstarind][-1]/(tov1.r[:tov1.Mstarind][-1] * (const.c**2))))

        print(phi_r[-1])
        # quit()

        for i in range(len(phi_r)-2, -1, -1):

            dphi_dr = (tov1.m[i] + (4*np.pi*(tov1.r[i]**3)*tov1.p[i]/(const.c**2))) / (tov1.r[i] * (tov1.r[i] - (2 * const.G * tov1.m[i] / (const.c**2))))
            phi_r[i] = phi_r[i+1] - dphi_dr

        print(phi_r)
        plt.scatter(tov1.r[:tov1.Mstarind], phi_r)
        # plt.xscale('log')
        plt.show()

        ### IS IT + or - ?????

        quit()
    # ?????

    # Section 7: Implement Epsilon
    if False:
        usr_unchecked1 = UserInput(const)
        usr_unchecked1.m_break = 4 * const.M_sun
        usr_unchecked1.rho_c = 1.9 * const.rho_nuc

        # --- NORMAL WITHOUT EPSILON---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            if tov1.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

        # --- NORMAL WITH EPSILON---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov2 = fcts.TOVmodel(usr1, const)
            fcts.rk1_incl_epsilon(usr1, const, tov2)

            if tov2.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov2.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov2.Pzero == False:
                print('M-BREAK REACHED')

        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun), label='Without ' r'$\epsilon$', linewidth=2)
        ax1.plot(const.R_sun_km * np.divide(tov2.r[:tov2.Mstarind], const.R_sun), np.divide(tov2.m[:tov2.Mstarind], const.M_sun), label='With ' r'$\epsilon$', linewidth=2)

        ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind], label='Without ' r'$\epsilon$', linewidth=2)
        ax2.plot(const.R_sun_km * np.divide(tov2.r[:tov2.Mstarind], const.R_sun), tov2.p[:tov2.Mstarind], label='With ' r'$\epsilon$', linewidth=2)

        ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='Without ' r'$\epsilon$')
        ax3.plot(const.R_sun_km * np.divide(tov2.r[:tov2.Mstarind], const.R_sun), np.divide(tov2.rho[:tov2.Mstarind], const.rho_nuc), label='With ' r'$\epsilon$')

        ax1.set_xscale('log')
        ax1.set_xlim(5e0, 2e1)
        ax2.set_xlim(5e0, 2e1)
        ax3.set_xlim(5e0, 2e1)
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        ax3.legend(title='gamma', loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_title('Mass of Object\nas function of Radius')
        ax2.set_title('Pressure of Object\nas function of Radius')
        ax3.set_title('Density of Object\nas function of Radius')
        ax1.set_ylabel('Mass  [' r'$M_{\odot}$' ']')
        ax2.set_ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
        ax3.set_ylabel('Density  [' r'$\rho_{nuc}$' ']')
        fig.tight_layout()
        plt.show()



        print('Difference in Mass and Radius')
        print('M1 = {0}'.format(np.divide(tov1.Mstar, const.M_sun)))
        print('R1 = {0}'.format(np.multiply(tov1.Rstar, 1e-5)))
        print('M2 = {0}'.format(np.divide(tov2.Mstar, const.M_sun)))
        print('R2 = {0}'.format(np.multiply(tov2.Rstar, 1e-5)))


    # Section 8: Netownian
    if False:
        usr_unchecked1 = UserInput(const)

        # so if rho_c is lower -> we need more iterations -> radius is bigger
        # --- Newtonian ---
        if True:
            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1_newtonian(usr1, const, tov1)

            if tov1.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov1.Mstar/const.M_sun))
                print('You set M_break = {0}'.format(usr1.m_break/const.M_sun))
                print('\n\n\n')
            elif tov1.Pzero == False:
                print('M-BREAK REACHED')

        # --- NORMAL ---
        if True:
            usr2 = check_userinput(const, defa, usr_unchecked1)
            tov2 = fcts.TOVmodel(usr2, const)
            fcts.rk1(usr1, const, tov2)

            if tov2.Pzero == True:
                print('\n\n\n')
                print('PRESSURE BELOW ZERO BEFORE M-BREAK REACHED -> ADJUST CENTRAL-DENSITY')
                print('M-star = {0} Msun'.format(tov2.Mstar/const.M_sun))
                print('You set M_brak = {0}'.format(usr2.m_break/const.M_sun))
                print('\n\n\n')
            elif tov2.Pzero == False:
                print('M-BREAK REACHED')


        plt.plot(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label='NEW')
        plt.plot(tov2.r[:tov2.Mstarind], tov2.m[:tov2.Mstarind], label='GR')
        plt.legend()
        plt.show()

        gs = gridspec.GridSpec(2, 2)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
        ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
        ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

        ax1.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.m[:tov1.Mstarind], const.M_sun), label='Newtonian')
        ax1.plot(const.R_sun_km * np.divide(tov2.r[:tov2.Mstarind], const.R_sun), np.divide(tov2.m[:tov2.Mstarind], const.M_sun), label='GR')

        ax2.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), tov1.p[:tov1.Mstarind], label='Newtonian')
        ax2.plot(const.R_sun_km * np.divide(tov2.r[:tov2.Mstarind], const.R_sun), tov2.p[:tov2.Mstarind], label='GR')

        ax3.plot(const.R_sun_km * np.divide(tov1.r[:tov1.Mstarind], const.R_sun), np.divide(tov1.rho[:tov1.Mstarind], const.rho_nuc), label='Newtonian')
        ax3.plot(const.R_sun_km * np.divide(tov2.r[:tov2.Mstarind], const.R_sun), np.divide(tov2.rho[:tov2.Mstarind], const.rho_nuc), label='GR')

        ax1.set_xscale('log')
        ax1.set_xlim(5e0, 2e1)
        ax2.set_xlim(5e0, 2e1)
        ax3.set_xlim(5e0, 2e1)
        ax2.set_xscale('log')
        ax3.set_xscale('log')
        ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.set_title('Mass of Object\nas function of Radius')
        ax2.set_title('Pressure of Object\nas function of Radius')
        ax3.set_title('Density of Object\nas function of Radius')
        ax1.set_ylabel('Mass  [' r'$M_{\odot}$' ']')
        ax2.set_ylabel('Pressure  [' r'$dyn \cdot cm^{-2}$' ']')
        ax3.set_ylabel('Density  [' r'$\rho_{nuc}$' ']')
        fig.tight_layout()
        plt.show()


        print('Difference in Mass and Radius')
        print('M1 = {0}'.format(np.divide(tov1.Mstar, const.M_sun)))
        print('R1 = {0}'.format(np.multiply(tov1.Rstar, 1e-5)))
        print('M2 = {0}'.format(np.divide(tov2.Mstar, const.M_sun)))
        print('R2 = {0}'.format(np.multiply(tov2.Rstar, 1e-5)))


    # NOW FOR MSTAR value -> plots of rho(r) and p(r) and
    if False:
        dep_var = np.linspace(1, 2.5, 20)
        models = []
        for var in dep_var:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.m_break = var * const.M_sun

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            models.append(tov1)

            if tov1.Mstar <= 0:
                print('MSTAR NOT REACHED!!!')
            else:
                print()
                print('{0} -- {1}'.format(round(var, 3), round(tov1.Mstar/const.M_sun, 3)))
                print(tov1.rho[tov1.Mstarind])
                print()
        quit()
        if True:
            gs = gridspec.GridSpec(2, 2)

            fig = plt.figure()
            ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
            ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
            ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

            for i,tov1 in zip(dep_var, models):
                ax1.plot(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label=str(i))
                ax2.plot(tov1.r[:tov1.Mstarind], tov1.p[:tov1.Mstarind], label=str(i))
                ax3.plot(tov1.r[:tov1.Mstarind], tov1.rho[:tov1.Mstarind], label=str(i))
            ax3.set_yscale('log')
            ax3.legend(title='M_star', loc='center left', bbox_to_anchor=(1, 0.5))
            ax1.set_title('Mass of Object\nas function of Radius')
            ax2.set_title('Pressure of Object\nas function of Radius')
            ax3.set_title('Density of Object\nas function of Radius')

            plt.show()



    # For different m_break plot rho_c vs radius
    # DEPENDENT-VARIABLE = m_break
    if False:
        dep_var = const.M_sun * np.linspace(1.0, 1.5, 5) # the dependent variable for many runs
        models = []
        for var in dep_var:
            # now we want to try many different rho_c
            # DEPENDENT-VARIABLE-2 = rho_c
            dep_var2 = np.linspace(5.0e14, 9.0e14, 10)
            r_star_vals = []
            for var2 in dep_var2:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.m_break = var
                usr_unchecked1.rho_c = var2

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                r_star_vals.append(tov1.Rstar)
            models.append([dep_var2, r_star_vals])

        for i, var in enumerate(models):
            plt.scatter(var[0], var[1], label=round(dep_var[i], 3))
        plt.legend(title='M-star break')
        plt.xlabel('rho_c [g cm-3]')
        plt.ylabel('R_star [R_sun]')
        plt.xscale('log')
        # plt.yscale('log')
        plt.show()

        # the plot before looks better, so don't choose this
        if False:
            for i, var in enumerate(models):
                plt.plot(var[1], var[0], label=round(dep_var[i], 3))
            plt.legend(title='M-star break')
            plt.ylabel('rho_c [g cm-3]')
            plt.xlabel('R_star')
            # plt.xscale('log')
            plt.yscale('log')
            plt.show()

    # For different Mstar values we want to plot all those things
    if False:
        # plot m(r), p(r), rho(r)

        usr_unchecked1 = UserInput(const)

        usr1 = check_userinput(const, defa, usr_unchecked1)
        tov1 = fcts.TOVmodel(usr1, const)
        fcts.rk1(usr1, const, tov1)

        fig, ax = plt.subplots(1, 3)
        ax[0].plot(tov1.r, tov1.m)
        ax[0].set_title('Mass of Object\nas function of Radius')
        ax[1].plot(tov1.r, tov1.p)
        ax[1].set_title('Pressure of Object\nas function of Radius')
        ax[2].plot(tov1.r, tov1.rho)
        ax[2].set_title('Density of Object\nas function of Radius')
        fig.tight_layout()
        plt.show()

    # Do the same as above but for different variables
    # FOR RHO_C
    if False:
        dep_var = np.logspace(14, 15, 10)
        models = []
        for var in dep_var:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.rho_c = var

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            models.append(tov1)

        fig, ax = plt.subplots(1, 3)
        for i,tov1 in zip(dep_var, models):
            ax[0].plot(tov1.r, tov1.m, label=str(i))
            ax[1].plot(tov1.r, tov1.p, label=str(i))
            ax[2].plot(tov1.r, tov1.rho, label=str(i))
        # ax[0].legend(title='rho_c')
        # ax[1].legend(title='rho_c')
        ax[2].legend(title='rho_c', loc='center left', bbox_to_anchor=(1, 0.5))
        ax[0].set_title('Mass of Object\nas function of Radius')
        ax[1].set_title('Pressure of Object\nas function of Radius')
        ax[2].set_title('Density of Object\nas function of Radius')
        # fig.tight_layout()
        plt.show()
    # FOR R0
    if False:
        dep_var = np.logspace(-10, 5, 10)
        models = []
        for var in dep_var:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.r0 = var

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            models.append(tov1)

        fig, ax = plt.subplots(1, 3)
        for i,tov1 in zip(dep_var, models):
            ax[0].plot(tov1.r, tov1.m, label=str(i))
            ax[1].plot(tov1.r, tov1.p, label=str(i))
            ax[2].plot(tov1.r, tov1.rho, label=str(i))
        # ax[0].legend(title='rho_c')
        # ax[1].legend(title='rho_c')
        ax[2].legend(title='r0', loc='center left', bbox_to_anchor=(1, 0.5))
        ax[0].set_title('Mass of Object\nas function of Radius')
        ax[1].set_title('Pressure of Object\nas function of Radius')
        ax[2].set_title('Density of Object\nas function of Radius')
        # fig.tight_layout()
        plt.show()
    # For K
    if False:
        # print(defa.m_break)
        dep_var = np.logspace(-7, -5, 10)
        models = []
        for var in dep_var:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.K = var

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)

            models.append(tov1)
            if tov1.Mstar <= 0:
                print('MSTAR NOT REACHED!!!')

        if False:
            fig, ax = plt.subplots(1, 3)
            for i,tov1 in zip(dep_var, models):
                ax[0].plot(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label=str(i))
                ax[1].plot(tov1.r[:tov1.Mstarind], tov1.p[:tov1.Mstarind], label=str(i))
                ax[2].plot(tov1.r[:tov1.Mstarind], tov1.rho[:tov1.Mstarind], label=str(i))
            # ax[0].legend(title='rho_c')
            # ax[1].legend(title='rho_c')
            ax[2].legend(title='K', loc='center left', bbox_to_anchor=(1, 0.5))
            ax[0].set_title('Mass of Object\nas function of Radius')
            ax[1].set_title('Pressure of Object\nas function of Radius')
            ax[2].set_title('Density of Object\nas function of Radius')
            # fig.tight_layout()
            plt.show()

        if True:
            gs = gridspec.GridSpec(2, 2)

            fig = plt.figure()
            ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
            ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
            ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns

            for i,tov1 in zip(dep_var, models):
                ax1.plot(tov1.r[:tov1.Mstarind], tov1.m[:tov1.Mstarind], label=str(i))
                ax2.plot(tov1.r[:tov1.Mstarind], tov1.p[:tov1.Mstarind], label=str(i))
                ax3.plot(tov1.r[:tov1.Mstarind], tov1.rho[:tov1.Mstarind], label=str(i))
            ax3.set_yscale('log')
            ax3.legend(title='K', loc='center left', bbox_to_anchor=(1, 0.5))
            ax1.set_title('Mass of Object\nas function of Radius')
            ax2.set_title('Pressure of Object\nas function of Radius')
            ax3.set_title('Density of Object\nas function of Radius')

            plt.show()




    # Then do the same as above but for comparing R_star


    # For different R_break plot M vs rho_c (need to change that it checks R_break to cut)
    if False:
        dep_var = const.R_sun * np.linspace(5e-6, 1e-5, 5) # the dependent variable for many runs
        models = []
        for var in dep_var:
            # now we want to try many different rho_c
            m_star_vals = []
            # DEPENDENT-VARIABLE-2 = rho_c
            dep_var2 = np.linspace(5.0e14, 9.0e15, 10)
            dep_var2 = np.logspace(np.log10(5.0e14), np.log10(9.0e15), 10)
            for var2 in dep_var2:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.cut_off = 'Radius'
                usr_unchecked1.r_break = var
                usr_unchecked1.rho_c = var2

                usr1 = check_userinput(const, defa, usr_unchecked1)
                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                # print(usr1.cut_off)
                # print(usr1.r_break)
                # print(tov1.m_break)

                m_star_vals.append(tov1.Mstar)
            models.append([dep_var2, m_star_vals])

        for i, var in enumerate(models):
            plt.plot(var[0], var[1], label='{0:3e}'.format(dep_var[i]))
        plt.legend(title='R-star break')
        plt.xlabel('rho_c [g cm-3]')
        plt.ylabel('M_star')
        # plt.xscale('log')
        # plt.yscale('log')
        plt.show()

    # For different RK methods plot accuracy and time
    if False:
        # dep_var = const.M_sun * np.linspace(1.0, 1.5, 5) # the dependent variable for many runs
        dep_var = [const.M_sun*3]
        models = []
        for var in dep_var:
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.m_break = var

            usr1 = check_userinput(const, defa, usr_unchecked1)
            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)
            tov2 = fcts.TOVmodel(usr1, const)
            fcts.rk2(usr1, const, tov2)
            tov3 = fcts.TOVmodel(usr1, const)
            fcts.rk3(usr1, const, tov3)
            tov4 = fcts.TOVmodel(usr1, const)
            fcts.rk4(usr1, const, tov4)

            models.append([tov1, tov2, tov3, tov4])

        for i, (var, cc) in enumerate(zip(dep_var, ['blue', 'red', 'green', 'black', 'orange'])):
            dats = models[i]
            plt.plot(dats[0].r[:dats[0].Mstarind], dats[0].m[:dats[0].Mstarind], label='{0}-RK1'.format(var))
            plt.plot(dats[1].r[:dats[1].Mstarind], dats[1].m[:dats[1].Mstarind], label='{0}-RK2'.format(var))
            plt.plot(dats[2].r[:dats[2].Mstarind], dats[2].m[:dats[2].Mstarind], label='{0}-RK3'.format(var))
            plt.plot(dats[3].r[:dats[3].Mstarind], dats[3].m[:dats[3].Mstarind], label='{0}-RK4'.format(var))
        plt.xscale('log')
        # plt.yscale('log')
        plt.legend()
        plt.show()

        # deviation from euler
        fig, ax = plt.subplots(2, 2, sharex=True)
        for ind_rk in range(0, 4):
            ax0 = ind_rk // 2
            ax1 = ind_rk%2
            for i, newm in enumerate(models):
                # eul = newm[0]
                eul = newm[ind_rk]
                ax[ax0][ax1].plot(newm[0].r[:newm[0].Mstarind], newm[0].m[:newm[0].Mstarind]-eul.m[:newm[0].Mstarind], label='RK1', linewidth=1)
                ax[ax0][ax1].plot(newm[1].r[:newm[1].Mstarind], newm[1].m[:newm[1].Mstarind]-eul.m[:newm[0].Mstarind], label='RK2', linewidth=1)
                ax[ax0][ax1].plot(newm[2].r[:newm[2].Mstarind], newm[2].m[:newm[2].Mstarind]-eul.m[:newm[0].Mstarind], label='RK3', linewidth=1)
                ax[ax0][ax1].plot(newm[3].r[:newm[3].Mstarind], newm[3].m[:newm[3].Mstarind]-eul.m[:newm[0].Mstarind], label='RK4', linewidth=1)
            ax[ax0][ax1].legend()


            # for i, newm in enumerate(models):
            #     # eul = newm[0]
            #     eul = newm[ind_rk]
            #     plt.scatter(newm[0].r[:newm[0].Mstarind], newm[0].m[:newm[0].Mstarind]-eul.m[:newm[0].Mstarind], label='RK1', s=0.3)
            #     plt.scatter(newm[1].r[:newm[1].Mstarind], newm[1].m[:newm[1].Mstarind]-eul.m[:newm[0].Mstarind], label='RK2', s=0.3)
            #     plt.scatter(newm[2].r[:newm[2].Mstarind], newm[2].m[:newm[2].Mstarind]-eul.m[:newm[0].Mstarind], label='RK3', s=0.3)
            #     plt.scatter(newm[3].r[:newm[3].Mstarind], newm[3].m[:newm[3].Mstarind]-eul.m[:newm[0].Mstarind], label='RK4', s=0.3)
            # plt.legend()
        plt.show()

    # determine R_star for different input parameters
    if False:
        # For self.K
        if True:
            dep_var = np.linspace(1.e-6, 3e-6, 10)
            res = []
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.K = dep_var

                usr1 = check_userinput(const, defa, usr_unchecked1)

                print(usr1.p_c)

                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)
                res.append(tov1.Rstar)

            plt.scatter(dep_var, res)
            plt.xlabel('K value')
            plt.ylabel('R_Star')
            plt.show()

        # For self.gamma

        # For self.rho_c

        # For


    ######## NEED TO INTRODUCE A CHECK FOR IF MSTAR OR RSTAR ARE REACHED!!! #########

    # so if we want to see how a variable affects it:

    # determine m(r), rho(r), p(r), .. as fct of all variables we can change (keeping rest constant)
    if False:
        #changing self.K = 1.982e-6
        if False:
            dep_var = np.linspace(8.0e-6, 1.0e-4, 30)
            dep_var = np.logspace(-8, -1, 40)
            models = []
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.K = var

                usr1 = check_userinput(const, defa, usr_unchecked1)

                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                models.append([tov1, usr1])

            for j in models:
                i = j[0]
                k = j[1]
                if i.Rstar <= 0:
                    print('\n\n\n ***** WARNING *****\nMStar not reached\n\n\n')
                    continue
                plt.plot(i.r[:i.Mstarind], i.m[:i.Mstarind]/const.M_sun, label = '{0:3e}'.format(k.K))

                print(k.K)
                # print(k.m_break)
                # print(i.Mstar)
                # print(k.r_break)
                print(i.Rstar)
                print()

                # print()

            plt.yscale('log')
            plt.legend()
            plt.show()
            quit()
                # plt.plot(i.r, i.m, label = '{0}'.format(str(k.K)))
                # print()
                # print(i.r)
                # print(i.m)
                # print(i.Mstar)
                # print(i.Rstar)
            plt.legend()
            plt.show()
            print(models.m)
            quit()

        # changing self.K but to find Mstar
        if False:
            dep_var = np.linspace(1e-8, 1.0, 40)
            dep_var = np.logspace(-8, -1, 40)
            print(dep_var)
            # quit()
            data = []
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.K = var

                usr1 = check_userinput(const, defa, usr_unchecked1)

                tov1 = fcts.TOVmodel(usr1, const)
                fcts.rk1(usr1, const, tov1)

                if tov1.Rstar <= 1:
                    continue
                else:
                    data.append([var, tov1.Rstar])

            data = np.array(data)
            ks = data[:,0]
            rs = data[:,1]
            plt.scatter(ks, rs)
            plt.plot(ks, rs)
            # also get default val
            usr_unchecked1 = UserInput(const)
            usr_unchecked1.K = defa.K

            usr1 = check_userinput(const, defa, usr_unchecked1)

            tov1 = fcts.TOVmodel(usr1, const)
            fcts.rk1(usr1, const, tov1)
            plt.scatter(defa.K, tov1.Rstar)

            plt.show()
            print(data.shape)
            print(data)
            quit()

        # changing r_0
        if False:
            dep_var = np.logspace(-10, 0, 20)
            models = []
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.r0 = var

                usr1 = check_userinput(const, defa, usr_unchecked1)

                tov1 = fcts.TOVmodel(usr1, const)

                fcts.rk1(usr1, const, tov1)

                models.append([tov1, usr1])

            # plot R vs M
            if False:
                for j in models:
                    i = j[0]
                    k = j[1]
                    if i.Rstar <= 0:
                        print('\n\n\n ***** WARNING *****\nMStar not reached\n\n\n')
                        continue
                    plt.plot(i.r[:i.Mstarind], i.m[:i.Mstarind]/const.M_sun, label = '{0:3e}'.format(k.r0))

                    print()
                    print(k.r0)
                    print(i.r[0])
                    print(i.Rstar/const.R_sun)
                plt.xscale('log')
                plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                plt.show()

            if False:
                r0s = []
                rstars = []
                for j in models:
                    i = j[0]
                    k = j[1]
                    if i.Rstar <= 0:
                        print('\n\n\n ***** WARNING *****\nMStar not reached\n\n\n')
                        continue

                    r0s.append(k.r0)
                    rstars.append(i.Rstar/const.R_sun)

                plt.scatter(r0s, rstars)
                plt.plot(r0s, rstars)
                plt.xscale('log')
                # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                plt.show()
            quit()

        # changing rho_c
        if True:
            dep_var = np.logspace(13, 18, 20)
            models = []
            for var in dep_var:
                usr_unchecked1 = UserInput(const)
                usr_unchecked1.rho_c = var

                usr1 = check_userinput(const, defa, usr_unchecked1)

                tov1 = fcts.TOVmodel(usr1, const)

                fcts.rk1(usr1, const, tov1)

                models.append([tov1, usr1])

            # plot R vs M
            if True:
                for j in models:
                    i = j[0]
                    k = j[1]
                    if i.Rstar <= 0:
                        print('\n\n\n ***** WARNING *****\nMStar not reached\n\n\n')
                        continue
                    plt.plot(i.r[:i.Mstarind], i.m[:i.Mstarind]/const.M_sun, label = '{0:3e}'.format(k.rho_c))

                    print()
                    print(k.rho_c)
                    print(i.rho[0])
                    print(i.Rstar/const.R_sun)
                # plt.xscale('log')
                plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                plt.show()

            if True:
                rho0s = []
                rstars = []
                for j in models:
                    i = j[0]
                    k = j[1]
                    if i.Rstar <= 0:
                        print('\n\n\n ***** WARNING *****\nMStar not reached\n\n\n')
                        continue

                    rho0s.append(k.rho_c)
                    rstars.append(i.Rstar/const.R_sun)

                plt.scatter(rho0s, rstars)
                plt.plot(rho0s, rstars)
                plt.xscale('log')
                # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                plt.show()

        #changing self.gamma = 2.75


    '''
        # determine R_star

        # determine central_density

        # Plot m(r)

        # Plot rho(r)

        # Plot P(r)

        # R_star(M_star)

        # M_star(rho_c) -- radius == const

        # rho_c(radius) -- mass == const

        # Runge-Kutta
    '''














    ######################################################################
    ######################################################################
    ######################################################################















    ##### ANALSIS
    # See how different rho_c changes M_star values
    # and do this for multiple m_break
    if False:
        m_break_vals = np.linspace(1.2, 1.8, 2)
        rho_vals = np.linspace(1e13, 1e16, 5)
        data = {}
        for i, mval in enumerate(m_break_vals):
            data[str(i)] = []
            for val in rho_vals:
                usr.rho_c = val
                usr.m_break = mval * const.M_sun
                usr = check_userinput(const, defa, usr)

                tov1 = fcts.TOVmodel(usr, const)
                fcts.rk4(usr, const, tov1)
                data[str(i)].append(tov1)

                for i,j in zip(tov1.r, tov1.m):
                    print(i, j)

        for i, mval in enumerate(m_break_vals):
            dat_mstar = [i.Mstar for i in data[str(i)]]
            plt.plot(rho_vals, dat_mstar, label = str(round(mval, 3)))
        plt.xlabel('Rho_c')
        plt.ylabel('M_star')
        # plt.yscale('log')
        plt.xscale('log')
        plt.legend(title='M_break Value')
        plt.show()


        for i, mval in enumerate(m_break_vals):
            dat_rstar = [i.Rstar for i in data[str(i)]]
            plt.plot(rho_vals, dat_rstar, label = str(round(mval, 3)))
        plt.xlabel('Rho_c')
        plt.ylabel('R_star')
        plt.legend(title='M_break Value')
        plt.show()


    #
    if False:
        m_break_vals = np.linspace(1.2, 1.8, 5)
        mbreak = []
        data = []
        for i, mval in enumerate(m_break_vals):
            # ** create user object
            usr_unchecked = UserInput(const)
            #
            usr.m_break = mval * const.M_sun
            usr = check_userinput(const, defa, usr)

            tov1 = fcts.TOVmodel(usr, const)
            fcts.rk4(usr, const, tov1)
            data.append(tov1)
            mbreak.append(usr.m_break)

        rhos = [i.rho for i in data]
        for j, i in enumerate(data):
            plt.plot(i.r,np.divide(i.rho, i.const.rho_nuc), label = m_break_vals[j], alpha=0.4)
        plt.xscale('log')
        plt.legend()
        plt.show()

        for j, i in enumerate(data):
            plt.plot(i.r,np.divide(i.m, i.const.M_sun), label = '{0}-Msun'.format(m_break_vals[j]), alpha=0.4)
        plt.legend()
        plt.xscale('log')
        plt.show()

        for j, i in enumerate(data):
            plt.plot(i.r/i.r_ss,np.divide(i.m, i.const.M_sun), label = '{0}-Msun'.format(m_break_vals[j]), alpha=0.4)
        plt.legend()
        plt.xscale('log')
        plt.show()

        for j, i in enumerate(data):
            plt.plot(i.r, i.p, label = m_break_vals[j], alpha=0.4)
        plt.legend()
        plt.show()
        quit()


        rstars = [i.Rstar for i in data]
        plt.scatter(mbreak, rstars)
        plt.xscale('log')
        plt.show()
        quit()

        for i, j in enumerate(data):
            plt.plot(j.r, j.m, label = str(m_break_vals[i]))
        plt.legend()
        plt.show()

        # rstars = [i.Rstar for i in data]

        # plt.plot(mbreak, rstars)
        # plt.xlabel('Break Mass M_break')
        # plt.ylabel('Star Radius R_star')
        # plt.show()




    if False:
        objs = []
        rho_vals = np.linspace(1e13, 1e16, 20)
        for val in rho_vals:
            usr.rho_c = val
            usr = check_userinput(const, defa, usr)

            tov1 = fcts.TOVmodel(usr, const)
            fcts.rk4(usr, const, tov1)
            objs.append(tov1)


        for i, j in enumerate(objs):
            plt.scatter(rho_vals[i], j.Mstar)

        plt.show()


    # for i, j in enumerate(objs):
    #     plt.plot(j.rho, j.m, label = rho_vals[i])
    #     # plt.plot(j.r, j.rho)
    #     # plt.plot(j.r, j.p)
    # plt.legend()
    # # plt.yscale('log')
    # # plt.xscale('log')
    # plt.show()





    if False:

        tov1 = fcts.TOVmodel(usr, const)
        tov2 = fcts.TOVmodel(usr, const)
        tov3 = fcts.TOVmodel(usr, const)
        tov4 = fcts.TOVmodel(usr, const)

        fcts.rk1(usr, const, tov1)
        fcts.rk2(usr, const, tov2)
        fcts.rk2(usr, const, tov3)
        fcts.rk4(usr, const, tov4)

        for x in [tov1, tov2, tov3, tov4]:
            plt.plot(x.r, x.rho)
        plt.title('rho vs r')
        plt.legend()
        plt.show()

        for x in [tov1, tov2, tov3, tov4]:
            plt.plot(x.r, x.m)
        plt.title('m vs r')
        plt.legend()
        plt.show()

        for x in [tov1, tov2, tov3, tov4]:
            plt.plot(x.r, x.p)
        plt.title('p vs r')
        plt.legend()
        plt.show()


    if False:
        tov1 = fcts.TOVmodel(usr, const)
        fcts.rk4(usr, const, tov1)


