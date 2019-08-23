using Entity;
using Microsoft.AspNet.SignalR;
using Repository;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace FireDetectionPortal.Controllers
{
    public class ApiController : Controller
    {
        INotificationRepository repo;

        public ApiController()
        {
            this.repo = new NotificationRepository();
        }

        [HttpPost]
        public JsonResult FireAlert()
        {
            try
            {
                foreach (String key in Request.Files)
                {
                    this.Save(Request.Files[key], Request["FireRate"],Request["Temp"],Request["SmokeRate"]);

                }
                Dictionary<string, string> result = new Dictionary<string, string>(){
                    {"status", "ok"}
                };
                return Json(result);
            }
            catch (Exception)
            {
                Dictionary<string, string> result = new Dictionary<string, string>(){
                    {"status", "fail"}
                };
                return Json(result);
                //throw ex;
            }
            
        }

        [NonAction]
        private void Save(HttpPostedFileBase image, string fireRate, string temp, string smokeRate)
        {
            Notification notification = new Notification();
            notification.ImageURL = "~/Images/" + image.FileName;
            notification.FireRate = float.Parse(fireRate);
            notification.SmokeRate = float.Parse(smokeRate);
            notification.Temp = float.Parse(temp);
            notification.Time = DateTime.Now;
            this.repo.Insert(notification);
            string path = Path.Combine(Server.MapPath("~/Images/"), image.FileName);
            image.SaveAs(path);
            this.SendNotification(float.Parse(fireRate), float.Parse(smokeRate), float.Parse(temp));
        }

        [NonAction]
        private void SendNotification(float fireRate, float smokeRate, float temp)
        {
            Dictionary<string, float> fireData = new Dictionary<string, float>(){
                {"fireRate", fireRate},
                {"smokeRate", smokeRate},
                {"temp", temp}
            };
            GlobalHost.ConnectionManager.GetHubContext<FireNotificationHub>().Clients.All.fireAlert(fireData);

        }
	}
}