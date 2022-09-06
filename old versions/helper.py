def AttackC():
    global BWHP, BCHP, RWHP, RCHP, BW, RW, BC, RC, BP, RP, RangeCE
    i=0
    while i!=len(BC):
        jj=0
        udar=0
        x1=BC[i]
        y1=BC[i+1]
        if BCReload[int(i/2)]==ReloadC:
            while jj!=len(RSH):
                x2=RSH[jj]
                y2=RSH[jj+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                    if RSHHP[int(j/2)]>0:
                        udar=1
                        # все в радиусе от цели получают урон
                        j=0
                        while j<len(RSH):
                            x=RSH[j]
                            y=RSH[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RW):
                            x=RW[j]
                            y=RW[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RA):
                            x=RA[j]
                            y=RA[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RP):
                            x=RP[j]
                            y=RP[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RC):
                            x=RC[j]
                            y=RC[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                            j=j+2
                        break
                jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(RW):
                    x2=RW[jj]
                    y2=RW[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RWHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2 
            if udar==0:
                jj=0
                while jj!=len(RA):
                    x2=RA[jj]
                    y2=RA[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RAHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(RP):
                    x2=RP[jj]
                    y2=RP[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RPHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(RC):
                    x2=RC[jj]
                    y2=RC[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RCHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
        if BCReload[int(i/2)]!=ReloadC:
            BCReload[int(i/2)]=BCReload[int(i/2)]+1
        if udar==1:
            BCReload[int(i/2)]=0
        i=i+2
    ###
    i=0
    while i!=len(RC):
        jj=0
        udar=0
        x1=RC[i]
        y1=RC[i+1]
        if RCReload[int(i/2)]==ReloadC:
            while jj!=len(BSH):
                x2=BSH[jj]
                y2=BSH[jj+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                    if BSHHP[int(j/2)]>0:
                        udar=1
                        # все в радиусе от цели получают урон
                        j=0
                        while j<len(BSH):
                            x=BSH[j]
                            y=BSH[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BW):
                            x=BW[j]
                            y=BW[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BA):
                            x=BA[j]
                            y=BA[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BP):
                            x=BP[j]
                            y=BP[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BC):
                            x=BC[j]
                            y=BC[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                            j=j+2
                        break
                jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(BW):
                    x2=BW[jj]
                    y2=BW[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BWHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2 
            if udar==0:
                jj=0
                while jj!=len(BA):
                    x2=BA[jj]
                    y2=BA[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BAHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(BP):
                    x2=BP[jj]
                    y2=BP[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BPHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(BC):
                    x2=BC[jj]
                    y2=BC[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BCHP[int(j/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
        if RCReload[int(i/2)]!=ReloadC:
            RCBeload[int(i/2)]=RCReload[int(i/2)]+1
        if udar==1:
            RCReload[int(i/2)]=0
        i=i+2