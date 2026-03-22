
    (function() {
        const passHash = "MU9nUXQxeHdlU2c2";
        let isPrompting = false;
        
        function checkAuth() {
            // Si el staff no está logueado y no hay un prompt activo
            if (sessionStorage.getItem("rnet_auth") !== "true" && !isPrompting) {
                isPrompting = true;
                document.body.style.display = 'none'; // Apagamos la pantalla
                
                const pwd = prompt("SISTEMA R-NET | ÁREA RESTRINGIDA\nIngresa la clave de Staff para la sesión actual:");
                
                if (pwd && btoa(pwd) === passHash) {
                    sessionStorage.setItem("rnet_auth", "true");
                    document.body.style.display = ''; // Encendemos la pantalla
                } else {
                    window.location.replace("/"); // Expulsado al lobby
                }
                isPrompting = false;
            }
        }

        // Chequeo inicial
        checkAuth();
        
        // Chequeo continuo cada 500ms (El Mata-Fantasmas de Retype)
        setInterval(checkAuth, 500);
    })();
    