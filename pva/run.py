from prisonapp import pva
import os

if __name__ == '__main__':
    #server.run()
    port = int(os.environ.get("PORT", 5000))
    pva.run(host='0.0.0.0', port=port)
