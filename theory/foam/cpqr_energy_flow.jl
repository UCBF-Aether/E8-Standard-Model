#!/usr/bin/env julia
# CPQR ENERGY FLOW — full ODE system: vortices → non-thermal → thermal.
using Printf

# Parameters (from CPQR)
L0 = 1.84e29; E_per_L = 8.71e4; E0 = E_per_L * L0
chi2 = 0.042; tau_th = 3.40e-25; a_rad = 7.5657e-16
fp = 0.7; ff = 0.3

function rhs!(dydt, y, t)
    Ev = y[1]
    L = Ev / E_per_L
    P_decay = E_per_L * chi2 * L^2
    dydt[1] = -P_decay
    dydt[2] = fp * P_decay - y[2] / tau_th
    dydt[3] = ff * P_decay - y[3] / tau_th
    dydt[4] = y[2] / tau_th + y[3] / tau_th
end

function rk4_step!(y, t, dt)
    k1=zeros(4); k2=zeros(4); k3=zeros(4); k4=zeros(4); yt=zeros(4)
    rhs!(k1, y, t)
    @. yt = y + 0.5*dt*k1; rhs!(k2, yt, t+0.5*dt)
    @. yt = y + 0.5*dt*k2; rhs!(k3, yt, t+0.5*dt)
    @. yt = y + dt*k3;     rhs!(k4, yt, t+dt)
    @. y = max(y + dt/6.0*(k1+2*k2+2*k3+k4), 0.0)
end

function run()
    println("="^70)
    println("CPQR ENERGY FLOW — vortices → non-thermal → thermal")
    println("="^70)
    println("  fp=$fp, ff=$ff, χ₂=$chi2, τ_th=$tau_th s\n")
    println("  t (s)         Evortex     Ephonon     Efermion    Ethermal    T_th(K)")
    y = [E0, 0.0, 0.0, 0.0]
    t = 1e-30; t_end = 1e-15; n_steps = 2000
    lts, lte = log10(t), log10(t_end)
    for i in 1:n_steps
        t_target = 10^(lts + (lte-lts)*i/n_steps)
        dt = t_target - t
        tau_d = 1/(chi2*(y[1]/E_per_L))
        n_sub = max(1, ceil(Int, dt/min(tau_th/5, tau_d/5, dt)))
        dts = dt/n_sub
        for _ in 1:n_sub; rk4_step!(y, t, dts); t += dts; end
        if i%200==0 || i==n_steps
            Tth = (y[4]/a_rad)^0.25
            println("  $(rpad(@sprintf("%.2e",t),12)) $(rpad(@sprintf("%.2e",y[1]),12)) $(rpad(@sprintf("%.2e",y[2]),12)) $(rpad(@sprintf("%.2e",y[3]),12)) $(rpad(@sprintf("%.2e",y[4]),12)) $(@sprintf("%.2e",Tth))")
        end
    end
    println("\n  Energy conservation: ratio=$(sum(y)/E0)")
    println("="^70)
end
run()
