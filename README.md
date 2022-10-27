# Metrics-Generator
Please check the task.txt file for the actual requirement of this work

1. Do a git clone to the main branch https://github.com/raajavel/vmware.git
2. cd vmware/metric-generator/src/
3. Build the docker file and push it to the local repository **``docker build -t -p 9090:8000 metric-generator```**
4. Apply the kubernetes yaml file **``kubectl apply -f .```**
5. All the metrics-generator, prometheus, grafana deplyments and services will be created.
6. run **``kubectl get svc -n vmware```**
7. Please check the ports in which the services are running. **localhost:<port>**
8. Add the target source in prometheus with the application port 
9. In th graph section of prometheus, seacrh for endpoint and you'll able to find 4 endpoint metrics populated, add them to panel.
10. Default login for grafana is username: admin password:admin. Reset the password after login
11. Create a Datasource, with prometheus as dataset and the target URL as **localhost:<port>** of prometheus
12. Create a Dashboard, select dataset as Prometheus, qery = endpoints name and save for all metrics.
  
  Sample screen shots are attached.
  
![prom_4](https://user-images.githubusercontent.com/66171070/198378830-81dc8591-048e-4bf3-a67a-d9ea0ae2f7e1.JPG)
![prom-1](https://user-images.githubusercontent.com/66171070/198378840-b8d9971d-211d-4ffa-8b68-06cd261224f3.JPG)
![promo_2](https://user-images.githubusercontent.com/66171070/198378846-1cb7c870-961e-4bf5-bcf9-c3e57ea308ca.JPG)
![grafana](https://user-images.githubusercontent.com/66171070/198378847-27a18138-00b7-4d17-9657-5095820760dc.JPG)
![kube](https://user-images.githubusercontent.com/66171070/198378852-7ac02e1b-e898-4232-aed2-c711842585be.JPG)
![prom_3](https://user-images.githubusercontent.com/66171070/198378854-1697650c-25cc-4b82-a3b3-e21f56d40b04.JPG)
