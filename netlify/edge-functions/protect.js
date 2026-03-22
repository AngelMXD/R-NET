
export default async (request, context) => {
    const url = new URL(request.url);
    
    
    if (url.pathname.toLowerCase().includes("guia-de-moderacion")) {
        const authHeader = request.headers.get("authorization");
        
        const expectedAuth = "Basic " + btoa("staff:FnxQT25njl");

        if (authHeader !== expectedAuth) {
            return new Response("Acceso Restringido al Staff de R-NET", {
                status: 401,
                headers: {
                    "WWW-Authenticate": 'Basic realm="Sistema R-NET (Usuario: staff)"'
                }
            });
        }
    }
    return context.next();
};
